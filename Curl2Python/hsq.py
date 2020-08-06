# -*- coding: utf-8 -*-
# @Time   : 2020/6/29 2:28 下午
# @Author : NewmanZhou
# @Desc : ==============================================
# Life is Short I Use Python!!!                      ===
# If this runs wrong,don't ask me,I don't know why;  ===
# If this runs right,thank god,and I don't know why. ===
# Maybe the answer,my friend,is blowing in the wind. ===
# ======================================================
# @Project : StudySpace
# @FileName: hsq.py
# @Software: PyCharm
import requests, re,json
from lxml import etree


def getListData():
    home_url = "http://haishengqian.com/index.php?r=l/d&u=1162970&id={}"
    headers = {
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    }

    params = (
        ('r', 'l'),
        ('page', '1'),
    )

    response = requests.get('http://haishengqian.com/index.php', headers=headers, params=params, verify=False)
    list_data = re.search('lsitData=([\s\S]+?);',response.text)[1]
    js_data = json.loads(list_data)
    for jd in js_data:
        jd["home_url"] = home_url.format(jd["id"])
        reqHomeUrl(jd)

def reqHomeUrl(jd):
    import requests

    cookies = {
        'dtk_satc_cid_v1130': '1593419727183',
        'MTA-USER-ID': '15affb53f729d1cd16a9971b542fa3ac',
        'DTK_SATC_REFERRER': 'http%3A//haishengqian.com/index.php%3Fr%3Dl%26page%3D1',
    }

    headers = {
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    }

    response = requests.get(jd["home_url"], headers=headers,
                           verify=False)
    html_tree = etree.HTML(response.text)
    xp = html_tree.xpath
    link_url = xp('//div[@class="buy-share"]/a/@href')[0]
    zhai_yao = xp('//div[@class="rec-text"]/span/text()')[0]
    jd["link_url"] = link_url
    jd["zhai_yao"] = zhai_yao
    print(jd)
    print('\n')

    'https://h5api.m.taobao.com/h5/mtop.user.getusersimple/1.0/?jsv=2.4.0&appKey=12574478&t=1593416489476&sign=0c18ebe943107ddf3f28c2767428a4c1&api=mtop.user.getUserSimple&v=1.0&H5Request=true&type=jsonp&dataType=jsonp&callback=mtopjsonp4&data=%7B%22isSec%22%3A0%7D'

if __name__ == '__main__':
    getListData()
