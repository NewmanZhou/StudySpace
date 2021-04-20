# -*- coding: utf-8 -*-
# @Time   : 2019/12/20 2:54 下午
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

import execjs
import requests
import json

def encodejs(querry):
    with open("baidujs.js",encoding="utf-8") as f:
        js_enrypt = f.read()

    encodejs = execjs.compile(js_enrypt)
    sign = encodejs.call("e",querry)
    return sign

def baiduquery(query):


    headers = {
        'authority': 'fanyi.baidu.com',
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'accept': '*/*',
        'origin': 'https://fanyi.baidu.com',
        'x-requested-with': 'XMLHttpRequest',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'referer': 'https://fanyi.baidu.com/translate?aldtype=16047&query=%E6%B5%8B%E8%AF%95%E6%95%B0%E6%8D%AE%0D%0A&keyfrom=baidu&smartresult=dict&lang=auto2zh',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'cookie': 'BIDUPSID=02D2AB73FFFE92179EEA945708B844C0; PSTM=1574646883; BAIDUID=02D2AB73FFFE9217E6E2F3BA8F3322F4:FG=1; H_WISE_SIDS=136722_128699_137484_139405_136896_128068_128144_139148_120199_138490_133994_138878_137985_137690_131247_132551_137745_136681_118880_118858_118842_118820_118791_138165_107313_138883_136430_138844_138697_139051_136862_138147_138114_139172_139593_136196_131862_137104_139276_139398_133847_138477_137734_138343_137467_138565_134256_138651_131423_139246_136164_137703_136751_110085_131113_139460_127969_139135_139162_139513_139409_127417_137186_136635_138425_138562_138943_138318_139222_138780_100458; delPer=0; H_PS_PSSID=1460_21092_30210_18560_30327_30283; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; from_lang_often=%5B%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; APPGUIDE_8_2_2=1; PSINO=2; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1576809868,1576831879; yjs_js_security_passport=dcb72e1f29b92cbfa2e9b9174b22f70d3c2af8f4_1576831880_js; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1576831894; __yjsv5_shitong=1.0_7_01f71cac7273d506de5f12609cd95595f050_300_1576831894264_124.127.104.130_3a0238b9; to_lang_often=%5B%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D',
    }

    params = (
        ('from', 'zh'),
        ('to', 'en'),
    )

    data = {
        'from': 'zh',
        'to': 'en',
        'query': query,
        'simple_means_flag': '3',
        'sign': encodejs(query),
        'token': '8b6d9c56c95e3815c831ff48e6f84122'
    }

    response = requests.post('https://fanyi.baidu.com/v2transapi', headers=headers, params=params, data=data)

    dict_data = json.loads(response.text)
    print(dict_data["dict_result"]["simple_means"]["word_means"][0])


def fanyi():
    import requests

    cookies = {
        'BIDUPSID': '61A2A56C52A95A7451B7E6A12A8C909A',
        'PSTM': '1617674951',
        'BAIDUID': '61A2A56C52A95A742C3A8CD677226B8F:FG=1',
        'BDORZ': 'B490B5EBF6F3CD402E515D22BCDA1598',
        '__yjs_duid': '1_3798492cd3b560f425279a6d733790bf1618294720777',
        'REALTIME_TRANS_SWITCH': '1',
        'FANYI_WORD_SWITCH': '1',
        'HISTORY_SWITCH': '1',
        'SOUND_SPD_SWITCH': '1',
        'SOUND_PREFER_SWITCH': '1',
        'H_PS_PSSID': '33801_33816_33746_33344_31254_33756_33675_33713_26350_22160',
        'delPer': '0',
        'PSINO': '2',
        'BA_HECTOR': '8g05ah250h2h24a0jo1g7cmon0q',
        'BAIDUID_BFESS': '61A2A56C52A95A742C3A8CD677226B8F:FG=1',
        'Hm_lvt_64ecd82404c51e03dc91cb9e8c025574': '1618313918,1618369381',
        'Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574': '1618369381',
        '__yjs_st': '2_YjEzNmNjODgzNjE5N2VkNzFkMzAxMGY0ODcyZjdmMDI0ZWFhYjBhZTNhNzYyZWJmZjg1NjEzMGRmNWNhOTc0ZTM1NzRmMDYwMTZiM2M3OGVhZTYwZDFkYzViYzYyMjkxM2VkYTc0NTRiMGZjYmY1ZDdlYTU1NzQ2ZDBmOGI4NDcyNTQyZWNiNzc4Mjg2M2UzM2QzYmY1MTkwY2M4ZTQ4OGQzM2ZjYzViMTY4OWY1YjM3ZjVkZjRiNGJiMTI5MDllNDZmYjkyYzUxNmYzODhhMDJiYTk2MTA5YzRiODU4MTUyNzAzYzY5ZjI5NThkNTA5OWUxMGM5MWZjODYzN2NkZl83XzYxMzYzNjg1',
        'ab_sr': '1.0.0_NmJhOTlkZmI3MDg0NDI3YWVjOGU3Zjc5ODIwMzQ0MjJkM2I1YjFhZDc4YjcyZjRjMjIyYWJmNmU2YzlkYmQyMzgwYzkzZDhmMjFkODYwMjViOGI1ZTUzOGMyN2U5MmVl',
    }

    headers = {
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua-mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Origin': 'https://fanyi.baidu.com',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://fanyi.baidu.com/',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    }

    data = {
        'kw': 'cat'
    }

    response = requests.post('https://fanyi.baidu.com/sug', headers=headers,data=data)
    dict_data = json.loads(response.text)
    print(dict_data)

if __name__ == '__main__':
    # print(encodejs("测试数据"))
    # baiduquery("测试")
    fanyi()