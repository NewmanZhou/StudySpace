#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/28 16:55
# @Author  : wjq
# @File    : zhihu.py

import json
from scrapy import Request
from pioneer_lib.define import ZHIHU_SITE_ID
from pioneer_lib.utils.others import extract_by_jpath
from pioneer_lib.utils.time_translater import nettime_to_pubtime
from pioneer_spider.spiders.custom_spider import CustomSpider


class ZhihuSpider(CustomSpider):
    name = 'zhihu'
    retry_proxy_http_codes = [302, 301]  # 知乎302 301反爬
    TOPIC_API = "https://www.zhihu.com/api/v4/topics/{}/feeds/timeline_activity?limit=20&offset=0"
    QUESTION_URL = "https://www.zhihu.com/question/{}"

    def start_requests(self):
        for _, extra_data in self.start_rule.get_start_url_datas():
            # extra_data = {
            #     "topic_id": 19585985,
            #     "topic_link": "https://www.zhihu.com/topic/19585985",
            #     "topic_name": "汽车行业"
            # }
            meta = {"extra_data": extra_data}
            yield Request(self.TOPIC_API.format(extra_data["topic_id"]),
                          meta=meta,
                          )

    def parse(self, response):
        json_datas = json.loads(response.text)
        extra_data = response.meta.get("extra_data")
        is_end = extract_by_jpath(json_datas, "$.paging.is_end")
        next_page = extract_by_jpath(json_datas, "$.paging.next")
        datas = extract_by_jpath(json_datas, "$.data")
        for data in datas:
            item = dict()
            item['platform_id'] = ZHIHU_SITE_ID
            item["extra_data"] = extra_data
            item["tags"] = [extra_data['topic_name']]
            item['topic_id'] = extra_data['topic_id']
            item["title"] = extract_by_jpath(data, "$.target.question.title")
            item["publish_time"] = extract_by_jpath(data, "$.target.question.created")
            item["article_id"] = extract_by_jpath(data, "$.target.question.id")
            item["article_url"] = self.QUESTION_URL.format(item["article_id"])
            if item["title"] is None:
                item["title"] = extract_by_jpath(data, "$..title")
                item["publish_time"] = extract_by_jpath(data, "$..created")
                item["article_id"] = extract_by_jpath(data, "$..id")
                item["article_url"] = self.QUESTION_URL.format(item["article_id"])

            item["publish_time"] = nettime_to_pubtime(item["publish_time"])
            if self.exceed(item["publish_time"]):
                break
            yield Request(item["article_url"], meta=item, callback=self.parse_user,
                          dont_filter=True)

        if not is_end:
            yield Request(next_page, meta=response.meta)

    def parse_user(self, response):
        data = response.xpath('//script[@id="js-initialData"]/text()').extract_first()
        json_data = json.loads(data)
        item = response.meta
        item['user_id'] = extract_by_jpath(json_data, "$..questions.{}.author.id".format(item["article_id"]))
        item["author_name"] = extract_by_jpath(json_data, "$..questions.{}.author.name".format(item["article_id"]))
        item["follower_count"] = extract_by_jpath(json_data,
                                                  "$..questions.{}.followerCount".format(item["article_id"]))  # 关注数量
        item["read_count"] = extract_by_jpath(json_data, "$..questions.{}.visitCount".format(item["article_id"]))
        item["comment_count"] = extract_by_jpath(json_data, "$..questions.{}.commentCount".format(item["article_id"]))
        item["reply_count"] = extract_by_jpath(json_data, "$..questions.{}.answerCount".format(item["article_id"]))
        item["tags"] = extract_by_jpath(json_data, "$..questions.{}.topics..name".format(item["article_id"]))
        yield item
