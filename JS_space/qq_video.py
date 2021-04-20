# -*- coding: utf-8 -*-
# @Time   : 2021/4/6 10:39 上午
# @Author : NewmanZhou
# @Desc : ==============================================
# Life is Short I Use Python!!!                      ===
# If this runs wrong,don't ask me,I don't know why;  ===
# If this runs right,thank god,and I don't know why. ===
# Maybe the answer,my friend,is blowing in the wind. ===
# ======================================================
# @Project : StudySpace
# @FileName: qq_video.py
# @Software: PyCharm

def getlist():
    import requests

    headers = {
        'authority': 'pbaccess.video.qq.com',
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
        'accept': '*/*',
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
        'origin': 'https://v.qq.com',
        'sec-fetch-site': 'same-site',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://v.qq.com/',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
    }

    params = (
        ('vcuid', '9000011676'),
        ('page_size', '30'),
        ('page', '1'),
        ('list_type', '1'),
    )

    response = requests.get(
        'https://pbaccess.video.qq.com/trpc.creator_center.header_page.personal_page/GetUserVideoList', headers=headers,
        params=params)

    print(response.text)

if __name__ == '__main__':
    getlist()