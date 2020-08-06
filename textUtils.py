# -*- coding: utf-8 -*-
"""
Created on Fri May 15 13:17:21 2020
@author: 李运辰
"""

import requests

requests.packages.urllib3.disable_warnings()
headers = {

    #
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.3",
}
headers2 = {
    # "Host":"music.liuzhijin.cn",
    "Host": "live.kuaishou.com",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.3",
    "Cookie": "did=web_c0f3196ec94d4837b5f7850e3ebac3b9; didv=1589520098000; clientid=3; client_key=65890b29",
}


def geturl(url0):
    # url0="https://v.kuaishou.com/5loz4u"
    res0 = requests.get(url0, headers=headers, verify=False)
    """转接第二段"""

    cookie = res0.cookies.get_dict()
    cookie = str(cookie).replace("{", "").replace("}", "").replace(" ", "").replace("'", "").replace(",", ";")

    headers3 = {
        "Host": "v.kuaishou.com",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.3",
        "Cookie": cookie.replace(":", "=")
    }

    headers4 = {
        "Host": "live.kuaishou.com",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.3",
        "Cookie": cookie.replace(":", "=")
    }
    res1 = requests.get(url0, headers=headers3, allow_redirects=False)
    url2 = res1.headers['Location']

    url_00 = url2.split("userId=")[1].split("&")[0]

    """第一部分url"""
    url_0 = url2.split("?")[0].split("/")[-1]
    res2 = requests.get(url2, headers=headers3, allow_redirects=False).request.headers

    """第二部分url"""
    url_1 = res2['Cookie'].split(";")[-1].replace(":", "=")

    """完整url"""
    url = "https://live.kuaishou.com/u/" + url_00 + "/" + url_0 + "?" + url_1
    # print(url)

    response = requests.get(url, headers=headers4)
    text = response.text
    print(text)
    """视频链接"""
    v_url = text.split('"playUrl":"')[1].split(".mp4")[0] + ".mp4"
    v_url = v_url.replace("u002F", "")
    # print(v_url)
    return v_url


st = "陪伴是最常情的告白，守护是最沉默的陪伴…… #汪星人 #宠物避障挑战 https://v.kuaishou.com/5xXNiL 复制此链接，打开【快手App】直接观看！"
st = "http" + (st.split("复制")[0].split("http")[1].replace(" ", ""))
u = geturl(st)
print(u)