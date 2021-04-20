# -*- coding: utf-8 -*-
# @Time   : 2021/3/1 1:57 下午
# @Author : NewmanZhou
# @Desc : ==============================================
# Life is Short I Use Python!!!                      ===
# If this runs wrong,don't ask me,I don't know why;  ===
# If this runs right,thank god,and I don't know why. ===
# Maybe the answer,my friend,is blowing in the wind. ===
# ======================================================
# @Project : StudySpace
# @FileName: dalipan.py
# @Software: PyCharm
import requests


def getList():
    headers = {
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'sec-ch-ua': '"Chromium";v="88", "Google Chrome";v="88", ";Not A Brand";v="99"',
        'Accept': 'application/json, text/plain, */*',
        'X-Authorization': '',
        'sec-ch-ua-mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36',
        'Origin': 'https://www.dalipan.com',
        'Sec-Fetch-Site': 'same-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://www.dalipan.com/',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    }

    params = (
        # ('t', '1614578106418'),
        ('kw', '小米'),
        ('page', '1'),
        ('line', '0'),
        ('site', 'dalipan'),
    )
    requests.adapters.DEFAULT_RETRIES = 5
    response = requests.get('https://api.dalipan.com/api/v1/pan/search', headers=headers, params=params, timeout=30)
    print(response.text)
    print('\n')
    print(response.status_code)

def baiduUrl():

    headers = {
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
        'Accept': 'application/json, text/plain, */*',
        'X-Authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1bmlvbmlkIjoib2JoZWFzOG1kUXJNQWUzZHZhdFZsMGJxMEpMbyIsImlhdCI6MTYxNDg0MjE0OSwiZXhwIjoxNjE2MDUxNzQ5fQ.YHmtYD5V1RuInRyA0yYxmmIR7rtHe9Cz8S7zMCDouXM',
        'sec-ch-ua-mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Safari/537.36',
        'Origin': 'https://www.dalipan.com',
        'Sec-Fetch-Site': 'same-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://www.dalipan.com/',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    }

    params = (
        ('id', 'b8b6062e04f13c91fd5c6ded13c337ec'),
    )

    response = requests.get('https://api.dalipan.com/api/v1/pan/url', headers=headers, params=params)

    print(response.text)

if __name__ == '__main__':
    # getList()
    baiduUrl()
