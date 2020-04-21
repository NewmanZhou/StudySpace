# -*- coding: utf-8 -*-
# @Time   : 2020/4/17 2:58 下午
# @Author : NewmanZhou
# @Desc : ==============================================
# Life is Short I Use Python!!!                      ===
# If this runs wrong,don't ask me,I don't know why;  ===
# If this runs right,thank god,and I don't know why. ===
# Maybe the answer,my friend,is blowing in the wind. ===
# ======================================================
# @Project : StudySpace
# @FileName: jeke.py
# @Software: PyCharm

def jeke():
    import requests

    cookies = {
        'gksskpitn': '380f7355-b9ae-4423-b0a3-94fe72f5aa7e',
        'SERVERID': '1fa1f330efedec1559b3abbcb6e30f50|1587106505|1587106337',
        'Hm_lvt_022f847c4e3acd44d4a2481d9187f1e6': '1587106338,1587106378,1587106506',
        'Hm_lpvt_022f847c4e3acd44d4a2481d9187f1e6': '1587106506',
        'LF_ID': '1587106338316-2978712-4623852',
        'GRID': '4fe1a62-106a8fd-395b495-1b6d66b',
        '_ga': 'GA1.2.116357930.1587106339',
        '_gid': 'GA1.2.1450467511.1587106339',
        'GCID': '4fe1a62-106a8fd-395b495-1b6d66b',
        'GCESS': 'BAcEtma3mAQEAC8NAAUEAAAAAAoEAAAAAAIESVKZXgkBAQsCBAADBElSmV4IAQMMAQEBBN7lGAAGBM5ccmA-',
    }

    headers = {
        'Host': 'time.geekbang.org',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:55.0) Gecko/20100101 Firefox/55.0',
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
        'Content-Type': 'application/json',
        'Referer': 'https://time.geekbang.org/column/article/188717',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
    }

    data = '{"id":"188717","include_neighbors":true,"is_freelyread":true}'

    response = requests.post('https://time.geekbang.org/serv/v1/article', headers=headers, cookies=cookies, data=data)
    print(response.text)


if __name__ == '__main__':
    jeke()