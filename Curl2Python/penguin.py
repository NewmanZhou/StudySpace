# -*- coding:utf-8 -*-

import os
import json
import copy
from urllib.parse import urljoin
from scrapy.http import Request, FormRequest

from pioneer_lib.logger.sentry_logging import log_mark
from pioneer_spider.spiders.custom_spider import CustomSpider
from pioneer_lib.utils.time_translater import nettime_to_pubtime
from pioneer_lib.utils.others import extract_by_jpath, get_sub_str_ex
from pioneer_lib.utils.html_clean import NewsCleanParser, combin_content, get_query_map
from scrapy.conf import settings


class PenguinSpider(CustomSpider):
    name = "penguin"
    # https://media.om.qq.com/6882593
    # https://media.om.qq.com/media/6882593/artilce/list
    ARTICLE_LIST_API = "https://media.om.qq.com/{mid}"
    ARTICLE_INFO_API = "http://kuaibao.qq.com/getSubNewsContent?id={}&style=json"
    ARTICLE_LIST_WAP_API = "https://kuaibao.qq.com/n/getMediaCardInfo?chlid={}"

    VIDEO_API = "http://h5vv.video.qq.com/getinfo?otype=json&platform=570701&vid={}"
    header = {
        'user-agent': 'Mozilla/5.0 (Macinstosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'cookie': 'ts_last=om.qq.com/userAuth/index'
    }
    custom_settings = {
        'DOWNLOAD_TIMEOUT': settings.get('MID_DOWNLOAD_TIMEOUT'),
        "DOWNLOADER_MIDDLEWARES": {
            "pioneer_spider.middlewares.ProxyPeopleMiddleware": 10,
            "pioneer_spider.middlewares.UserAgentMiddleware": 20,
            'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
        },
    }

    def start_requests(self):
        # meta_data = {"extra_data": {}, "page": 1}
        # yield FormRequest(
        #     url='https://media.om.qq.com/media/6882593/artilce/list',
        #     headers=self.header,
        #     formdata={'page':'1', '_csrf':''},
        #     meta=meta_data
        # )

        for _, extra_data in self.start_rule.get_start_url_datas():

            meta_data = {"extra_data": extra_data, "page": 1}

            article_list_url = self.get_articles_url(extra_data["user_id"])
            #yield Request(article_list_url, meta=meta_data)
            yield FormRequest(
                url='https://media.om.qq.com/media/{}/artilce/list'.format(extra_data["user_id"]),
                headers=self.header,
                formdata={'page': '1', '_csrf': ''},
                meta=meta_data
            )
            yield Request(self.ARTICLE_LIST_WAP_API.format(extra_data["user_id"]), callback=self.parse_wap_home,
                          meta={"extra_data": extra_data},
                          headers={'referer': 'https://kuaibao.qq.com/media/{}'.format(extra_data["user_id"])})

    def parse_mp_home(self, response):
        j_data = json.loads(response.text)
        if j_data.get('retcode') == 100001 and j_data.get('retmsg'):
            # {'retcode': 100001, 'retmsg': 'schema: error converting value for "uin"'}
            str_log = "retmsg:" + j_data['retmsg'] + "具体的url:" + response.url
            log_mark(loginfo=str_log, source='企鹅号')

        articles = extract_by_jpath(j_data, "$.result.articleinfos")
        for art_info in articles:
            item = dict()
            art_url = extract_by_jpath(art_info, "$.articleurl")
            item["extra_data"] = response.meta["extra_data"]
            art_id = get_query_map(art_url).get("query", {}).get("article_id")
            if not art_id:
                continue
            item["article_id"] = art_id
            item["title"] = extract_by_jpath(art_info, "$.title")
            item["article_url"] = art_url
            # item["visitor_count"]
            item["comment_count"] = extract_by_jpath(art_info, "$.commentCount")
            item["fans_num"] = extract_by_jpath(art_info, "$.likeCount")

            item["publish_time"] = nettime_to_pubtime(extract_by_jpath(art_info, "$.timeTips"))
            if self.exceed(item["publish_time"]):
                break
            meta = copy.deepcopy(response.meta)
            meta["item"] = item
            yield Request(item["article_url"],
                          meta=meta,
                          callback=self.parse_mp_article)

    def parse(self, response):
        dom = response.xpath('//*[@class="media-content"]')
        if not dom:  # 打开登录界面 todo 验证后不发article_list_url
            str_log = "article_list_url可能打开登录界面, 具体的url:" + response.url
            log_mark(loginfo=str_log, source='企鹅号')
        bstop = False
        bdata = False
        last_time = response.meta.get('publish_time')
        publish_time = ''
        for elem_media in dom:
            bdata = True
            artical_link = elem_media.xpath('*[@class="media-heading"]/a/@href').extract()[0]
            publish_time = \
                elem_media.xpath('*[@class="media-status"]/span[@class="media-status-text"]/text()').extract()[0]
            if self.exceed(publish_time):
                bstop = True
                break
            yield Request(self.ARTICLE_INFO_API.format(os.path.basename(artical_link)),
                          callback=self.parse_article,
                          meta=response.meta)
        extra_data = response.meta.get("extra_data")
        page = response.meta.get("page")
        if not bstop and publish_time and last_time != publish_time:
            page += 1
            yield FormRequest(
                url='https://media.om.qq.com/media/{}/artilce/list'.format(extra_data["user_id"]),
                # url='https://media.om.qq.com/media/6882593/artilce/list',
                headers=self.header,
                formdata={'page': str(page), '_csrf': ''},
                meta={"extra_data": extra_data, "page": page, 'publish_time': publish_time}
            )
        if not bdata and page == 1:
            home_url = "https://kandian.qq.com/cgi-bin/social/" \
                       "getHomePage?pageSize=10&tabid=0&uin={}".format(extra_data["user_id"])
            meta_data = {"extra_data": extra_data}
            yield Request(home_url, meta=meta_data, callback=self.parse_mp_home)

    def parse_mp_article(self, response):
        item = response.meta["item"]
        try:
            item["visitor_count"] = int(response.xpath('//*[@id="mod-common"]/@data-pv').extract()[0])
        except:
            pass
        news_clean = NewsCleanParser()
        content, images, _ = news_clean.content_clean(response.text)
        sort_imgs = sorted(images.items(), key=lambda v: v[0])
        imgs = []
        for v in sort_imgs:
            img_url = v[-1]["src"]
            scheme = get_query_map(img_url).get("scheme")
            if not scheme:
                img_url = "http:%s" % img_url
            imgs.append(img_url)
        item["images"] = imgs
        item["content"] = combin_content(content, item["images"])
        yield item

    def parse_article(self, response):
        value = json.loads(response.text)

        item = dict()
        item["extra_data"] = response.meta.get("extra_data")

        item["article_id"] = extract_by_jpath(value, "$.id")
        # item["user_id"] = extract_by_jpath(value, "$.card.chlid")
        # item["source"] = extract_by_jpath(value, "$card.chlname")

        item["publish_time"] = nettime_to_pubtime(extract_by_jpath(value, "$.pub_time"))
        item["top_image"] = extract_by_jpath(value, "$.imgurl")
        item["title"] = extract_by_jpath(value, "$.title")
        item["videos"] = extract_by_jpath(value, "$.body.videos[:].ums_id", True)
        item["images"] = extract_by_jpath(value, "$.attribute..url", True)
        item["field"] = extract_by_jpath(value, "$.category")
        item["original_flg"] = extract_by_jpath(value, "$.isOriginal")
        item["visitor_count"] = extract_by_jpath(value, "$.count_info.playcount")
        item["comment_count"] = extract_by_jpath(value, "$.count_info.comments")

        img_patten = r"<[p|P]><!--IMG_\d+--></[p|P]>"

        item["content"] = combin_content(extract_by_jpath(value, "$.content.text"), item["images"], img_patten)
        item["abstract"] = extract_by_jpath(value, "$.abstract")
        item["article_url"] = "https://kuaibao.qq.com/s/{}".format(item["article_id"])

        video_flg = value.get("isVideoAritcle")
        if video_flg:
            item["videos"] = [extract_by_jpath(value, "$.short_url")]
            item["content"] = None
        #     video_id = extract_by_jpath(value, "$.attribute.VIDEO_0.vid")
        #
        #     yield Request(self.VIDEO_API.format(video_id),
        #                   callback=self.parse_video,
        #                   meta={"item":item, "vid":video_id})
        #
        # else:
        #     yield item
        yield item

    def parse_video(self, response):
        video_id = response.meta["vid"]
        item = response.meta["item"]
        j_data = json.loads(next(get_sub_str_ex(response.text, "QZOutputJson=", ";", True)))

        for v_data in extract_by_jpath(j_data, "$.vl.vi[]"):
            fp_datas = sorted(v_data.get("ul", {}).get("ui", []), key=lambda v: v["vt"], reverse=True)
            video_url = urljoin(fp_datas[0].get("url"),
                                "{v_id}.mp4?vkey={v_key}".format(v_id=video_id, v_key=v_data["fvkey"]))
            item["videos"] = [video_url]
            break
        item["content"] = None
        yield item

    def parse_wap_home(self, response):
        rj = json.loads(response.text)
        for i in extract_by_jpath(rj, 'info.[newsList,videoList]'):
            for value in i:
                publish_time = nettime_to_pubtime(extract_by_jpath(value, "timestamp"))
                if self.exceed(publish_time):
                    break
                item = dict()
                item["extra_data"] = response.meta.get("extra_data")
                article_id = extract_by_jpath(value, "$.id")
                item["article_id"] = article_id
                item["publish_time"] = publish_time
                item["title"] = extract_by_jpath(value, "$.title")
                item["article_url"] = "https://kuaibao.qq.com/s/{}".format(item["article_id"])
                yield Request(self.ARTICLE_INFO_API.format(article_id),
                              callback=self.parse_article,
                              meta={"extra_data": response.meta["extra_data"], "item": item})
