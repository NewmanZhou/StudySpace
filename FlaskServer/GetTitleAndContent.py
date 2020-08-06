# -*- coding: utf-8 -*-
# @Time   : 2020/8/6 9:06 下午
# @Author : NewmanZhou
# @Desc : ==============================================
# Life is Short I Use Python!!!                      ===
# If this runs wrong,don't ask me,I don't know why;  ===
# If this runs right,thank god,and I don't know why. ===
# Maybe the answer,my friend,is blowing in the wind. ===
# ======================================================
# @Project : StudySpace
# @FileName: GetTitleAndContent.py
# @Software: PyCharm
from readability.readability import Document
import urllib3, re, html2text, json

from lxml import etree


class GetTitleAndContent(object):

    def __init__(self):
        self.ht = html2text.HTML2Text()
        self.ht.ignore_links = True
        self.ht.ignore_images = False
        self.ht.ignore_emphasis = True
        self.ht.ignore_tables = True
        self.http = urllib3.PoolManager()

    def getTitleAndContent(self, contentUrl):
        myHeader = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:55.0) Gecko/20100101 Firefox/55.0',
        }
        try:
            r = self.http.request('GET', contentUrl, headers=myHeader)
            # print(r.status)  # 200
            # 获得html源码,utf-8解码
            # print(r.data.decode())
            html = r.data
            readable_tilte = Document(html).short_title()
            readable_article = Document(html).summary()
            content = self.ht.handle(readable_article)
            # content = re.sub(r'阅读剩余全文（）|该菜谱创建于[\s\S]+任何部分的内容。|(更多相关资讯请关注：|用手机访问|1[\s\d]+\s下一页|\*\s|精美图片)[\s\S]+|(新闻热线：[\s\S]+)#', '', content)

            response = etree.HTML(html)
            # content = response.xpath("string(//div[@class='text-3zQ3cZD4'])")
            # content = re.sub(
            #     r'图集|(\+1\s|【纠错】)[\s\S]+', '',
            #     content).strip()
            # script = response.xpath("//script")[5].text
            # response = re.findall('contentList":([\s\S]+),"currentPage', script)[0]
            # datas = json.loads(response)[0]
            # strData = datas['data']

            # pat = re.compile('<[^>]+>', re.S)
            # content = pat.sub('', strData)
            # content = ''.join(content).replace(u'\u3000', '').replace(u'\xa0','').strip()
            data = dict()
            data["title"] = readable_tilte
            data["content"] = content

            return self.return_data(0, "success", data)
        except Exception as e:
            return self.return_data(1, e)

    def return_data(self, code, msg, data=dict()):
        return_dict = {
            "code": code,
            "msg": msg,
            "data": data,
        }
        return json.dumps(return_dict)

# myClass = GetTitleAndContent()
# data = myClass.getTitleAndContent('https://news.e23.cn/wanxiang/2020-08-06/2020080600616.html')
# print(data)