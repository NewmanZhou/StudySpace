# -*- coding: utf-8 -*-
# @Time   : 2021/2/18 2:48 下午
# @Author : NewmanZhou
# @Desc : ==============================================
# Life is Short I Use Python!!!                      ===
# If this runs wrong,don't ask me,I don't know why;  ===
# If this runs right,thank god,and I don't know why. ===
# Maybe the answer,my friend,is blowing in the wind. ===
# ======================================================
# @Project : StudySpace
# @FileName: Xdaili.py
# @Software: PyCharm
import requests
import urllib3
import sys, time, hashlib


def XdailiTest():

    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    _version = sys.version_info

    is_python3 = (_version[0] == 3)

    orderno = "ZF20212183665Ed5nW3"
    secret = "929b51ac17ac4b11b70aac963e31dd50"

    ip = "forward.xdaili.cn"
    port = "80"

    ip_port = ip + ":" + port

    timestamp = str(int(time.time()))
    string = ""
    string = "orderno=" + orderno + "," + "secret=" + secret + "," + "timestamp=" + timestamp

    string = string.encode()

    md5_string = hashlib.md5(string).hexdigest()
    sign = md5_string.upper()
    # print(sign)
    auth = "sign=" + sign + "&" + "orderno=" + orderno + "&" + "timestamp=" + timestamp

    # print(auth)
    proxy = {"http": "http://" + ip_port, "https": "https://" + ip_port}

    headers = {
        'Proxy-Authorization': auth,
        'sec-ch-ua': '"Chromium";v="88", "Google Chrome";v="88", ";Not A Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
        'Referer': 'https://www.dalipan.com/',
    }

    url = "https://www.dalipan.com/search?keyword=康宝莱"
    # url = "http://www.dalipan.com/search?keyword=三一重工&page=1"
    response = requests.get(url, headers=headers, proxies=proxy, verify=False, allow_redirects=False)

    print(response.text)


if __name__ == '__main__':
    XdailiTest()
