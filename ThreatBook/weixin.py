# -*- coding: utf-8 -*-
# @Time   : 2021/3/8 3:05 下午
# @Author : NewmanZhou
# @Desc : ==============================================
# Life is Short I Use Python!!!                      ===
# If this runs wrong,don't ask me,I don't know why;  ===
# If this runs right,thank god,and I don't know why. ===
# Maybe the answer,my friend,is blowing in the wind. ===
# ======================================================
# @Project : StudySpace
# @FileName: weixin.py
# @Software: PyCharm

def getList():
    import requests

    headers = {
        'authority': 'mp.weixin.qq.com',
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
        'x-requested-with': 'XMLHttpRequest',
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Safari/537.36',
        'accept': '*/*',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://mp.weixin.qq.com/cgi-bin/appmsg?t=media/appmsg_edit_v2&action=edit&isNew=1&type=10&createType=10&token=136317860&lang=zh_CN',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'cookie': 'ua_id=9FYko8xBw48gYj28AAAAAJXYVxujV-ABOUbiGbIte7s=; uuid=155dc234fe3e40315fada966dd64904e; rand_info=CAESIEeW4jkog0WLyENdZfn1PkRr9++3F9pFhh8a6EbU3hkS; slave_bizuin=3924221110; data_bizuin=3924221110; bizuin=3924221110; data_ticket=vQVwh+YGhb2hmN3iO3OALi1UUyXZwD8sdBknN17pjsliBeQSnlEwvg9WnwGzvj+U; slave_sid=R3dXUDBocHhSRTNZU3RLUENyRmFiNEdMTlc1RmNNZ2FaMU9KTXJQMUpPOTFlblBYVWZrallic1BrcGEycDNjVkdwUWhnY2hUU1NvMldvNU9qWFo2bTQwZm16MFc3Z1pMUFNpQTBMd1BhTU0yZlZPZUJoYkhwRHN1MFZUbXFzTXdEY09qcWZJVjZNZnV1T1N1; slave_user=gh_179d2ed1dd07; xid=4ed4d85b91e670691ede17d478388147; openid2ticket_ottzm6YLqMN1gln4WfJX2bxtBkYc=; mm_lang=zh_CN',
    }

    params = (
        ('action', 'list_ex'),
        ('begin', '10'),
        ('count', '5'),
        ('fakeid', 'MzA5NzgzODI5NA=='),
        ('type', '9'),
        ('query', ''),
        ('token', '136317860'),
        ('lang', 'zh_CN'),
        ('f', 'json'),
        ('ajax', '1'),
    )

    response = requests.get('https://mp.weixin.qq.com/cgi-bin/appmsg', headers=headers, params=params)

    print(response.text)


if __name__ == '__main__':
    getList()
