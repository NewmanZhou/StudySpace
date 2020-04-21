# -*- coding: utf-8 -*-
# @Time   : 2020/4/14 3:31 下午
# @Author : NewmanZhou
# @Desc : ==============================================
# Life is Short I Use Python!!!                      ===
# If this runs wrong,don't ask me,I don't know why;  ===
# If this runs right,thank god,and I don't know why. ===
# Maybe the answer,my friend,is blowing in the wind. ===
# ======================================================
# @Project : StudySpace
# @FileName: getContentNum.py
# @Software: PyCharm

import requests, re, json, random


def readText(filename):
    with open(filename, "r") as file:
        lines = file.readlines()
        fp = open("successfile.txt", "a+", encoding="utf-8")
        for line in lines:

            # print(type(line), line)
            # 过滤地址
            if "toutiao" in line:
                count = mChrome(line)
                fp.write(str(count))
                fp.write("\n")
                fp.seek(0, 0)
            else:
                fp.write("-1")
                fp.write("\n")
                fp.seek(0, 0)
        fp.close()


def mChrome(url):
    id = re.search("(\d{10,})", url)[1]
    baseUrl = "https://m.toutiao.com/i{}/info/".format(id)
    headers = {
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Mobile Safari/537.36',
        'Sec-Fetch-Dest': 'document',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-Mode': 'navigate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    }
    response = requests.get(baseUrl, headers=headers)
    print(response.text)
    print(response.status_code)
    json_data = json.loads(response.text)
    content = json_data["data"]["content"]
    hans_total = hans_count(content)
    # print(content)
    print(hans_total)
    return hans_total

def hans_count(str):
    hans_total = 0
    for s in str:
        # 中文字符其实还有很多，但几乎都用不到，这个范围已经足够了
        if '\u4e00' <= s <= '\u9fef':
            hans_total += 1
    return hans_total


def getProxy():
    data = requests.get("http://39.105.14.86:8090/getallproxys")
    response = json.loads(data.text)
    data = response["data"]
    proxyip = random.choice(data)
    proxy_dict = {
        "http": "http://{}".format(proxyip),
        "https": "https://{}".format(proxyip),
    }
    return proxy_dict

if __name__ == '__main__':
    # readText("excel.text")
    url = "https://www.toutiao.com/i6802961699113533955"
    mChrome(url)
