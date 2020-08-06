# -*- coding: utf-8 -*-
# @Time   : 2020/4/27 2:01 下午
# @Author : NewmanZhou
# @Desc : ==============================================
# Life is Short I Use Python!!!                      ===
# If this runs wrong,don't ask me,I don't know why;  ===
# If this runs right,thank god,and I don't know why. ===
# Maybe the answer,my friend,is blowing in the wind. ===
# ======================================================
# @Project : StudySpace
# @FileName: baidu.py
# @Software: PyCharm

import re
import time
import urllib3
import requests
from pymongo import MongoClient
from lxml import etree
from datetime import datetime, timedelta

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def getBaiduFirstPager(pn):


    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
        'Connection': 'keep-alive',
        'DNT': '1',
        'Host': 'www.baidu.com',
        'Referer': 'https://www.baidu.com/s?rtt=1&bsst=1&cl=2&tn=news&word=%E4%BC%98%E6%83%A0%E5%88%B8',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:55.0) Gecko/20100101 Firefox/55.0',
    }

    # 按时间排序爬取 rtt : 4 时间， 1 焦点
    req_url = "https://www.baidu.com/s?cl=2&medium=0&rtt=4&bsst=1&tn=news&word=%E6%B6%88%E8%B4%B9%E5%88%B8&pn={}"
    response = requests.get(req_url.format(pn), headers=headers, verify=False, timeout=10)
    res = etree.HTML(response.text)
    datas = res.xpath('//div[@id="content_left"]//div[@class="result"]')
    for data in datas:
        item = dict()
        item["title"] = data.xpath('string(h3)').strip()
        source_text = data.xpath('string(div//p[@class="c-author"])')
        source_list = re.split('\s{2,}', source_text.strip())
        item["source"] = source_list[0]
        item["time"] = my_conv_time(source_list[1])
        item["url"] = data.xpath('h3[@class="c-title"]/a/@href')[0]
        print(item)
        collection.save(item)
    try:
        nextpager = res.xpath('//p[@id="page"]/strong/span[@class="pc"]/text()')[0]
        nextpagernum = int(nextpager)*10
        re.search("下一页",response.text)[0]
        getBaiduFirstPager(str(nextpagernum))
    except TypeError:
        print("采集结束")



def conv_time(t):
    min = int(re.findall('\d+', t)[0])
    if '秒' in t:
        s = (datetime.now() - timedelta(seconds=min))
    elif '分钟' in t:
        s = (datetime.now() - timedelta(minutes=min))
    elif '小时' in t:
        s = (datetime.now() - timedelta(hours=min))
    elif '天' in t:
        s = (datetime.now() - timedelta(days=min))
    else:
        # current_year = datetime.today().strftime("%Y")
        # t += ", " + current_year
        # s = datetime.strptime(t, "%m-%d, %Y")
        return t
    return s
def my_conv_time(time_str):
    try:
        data = conv_time(time_str).timetuple()
        end_time = time.strftime("%Y年%m月%d日 %H:%M", data)
        return end_time
    except:
        return time_str



if __name__ == '__main__':
    '''
    root  123456
    "mongodb://用户名:密码@公网ip:端口/"
    '''

    uri = 'mongodb://%s:%s@%s:%s/%s' % ('root','123456','10.50.162.87', 27017, 'admin')
    mgdb = MongoClient(uri, connect=False, maxPoolSize=5000).get_database('test')
    # 指定集合
    collection = mgdb.baidu


    getBaiduFirstPager("0")
