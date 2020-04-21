# -*- coding: utf-8 -*-
# @Time   : 2020/3/26 1:35 下午
# @Author : NewmanZhou
# @Desc : ==============================================
# Life is Short I Use Python!!!                      ===
# If this runs wrong,don't ask me,I don't know why;  ===
# If this runs right,thank god,and I don't know why. ===
# Maybe the answer,my friend,is blowing in the wind. ===
# ======================================================
# @Project : StudySpace
# @FileName: qeh_qq_kuaibao.py
# @Software: PyCharm

import random
DATA = "".join(random.choice("123456789") for i in range(15))
def getSubNewsIndex():
    import requests

    cookies = {
        'lskey': '',
        'luin': '',
        'skey': '',
        'uin': '',
        'kb_qbid': '',
        'qb_guid': 'e9234a46039624c2594ff227377988cb',
        'qb_qua': 'QV=3&PL=ADR&PR=KB&PP=com.tencent.reading&PPVN=6.2.30.0&CO=SYS&PB=GE&VE=P&DE=PHONE&CHID=70307&LCID=0&MO= PRO5 &RL=1080*1920&OS=5.1&API=22&REF=qb_0&TM=00',
        'logintype': '0',
    }

    headers = {
        'Host': 'r.cnews.qq.com',
        'Referer': 'http://cnews.qq.com/cnews/android/',
        'User-Agent': '%E7%9C%8B%E7%82%B9%E5%BF%AB%E6%8A%A56230(android)',
        'snqn': 'FNa1VcUgoqyy/ojgQrUqNOdsbGSoJBXwuTaQD7Rn271QCUY2rSoI2kAfQd5sYf4MSpmf+9Btu5sY1pqj36GkfCkUmBaNZPNVHqcn5+wozqS4KqcrHEH3V5F4TFBO3qKkFNW7ZuK5CQpQTl9h9hyarQ==',
        'svqn': '1_4',
        'qn-sig': 'ce61cd1d81c44278842c61209203a560',
        'qn-rid': '1a8275d4-7182-4337-9e4f-7f387e19ce03',
    }

    params = (
        ('devid', DATA),
    )

    data = {
        # 'cityList': '',
        # 'isUpdatingLocation': '1',
        # 'REQBuildTime': '1585201252740',
        # 'ssid': '<unknown ssid>',
        # 'omgid': '',
        # 'REQExecTime': '1585201252740',
        # 'qqnetwork': 'wifi',
        # 'commonsid': 'a389e0b410e249e6b99aff24e9780fc8',
        # 'kingCardType': '0',
        # 'format': 'json',
        # 'picSizeMode': '0',
        # 'commonGray': '1_3|2_0|18_1|12_0|22_1|49_0|47_1|14_0|17_0|30_0|42_0|99_0',
        # 'currentTab': 'kuaibao',
        # 'proxy_addr': '172.30.6.19:8888',
        # 'is_wap': '0',
        # 'lastCheckCardType': '0',
        # 'omgbizid': '',
        # 'imsi': '',
        # 'commonIsFirstLaunch': '0',
        # 'chlidType': '0',
        # 'taid': '0101869F9CFE37D73B68DC94E0869278F6341C23C23AB3665B04598DAFED432764555F65EC4CF248F523DA5B',
        # 'activefrom': 'icon',
        # 'media_openid': '',
        # 'unixtimesign': '1585201252743',
        # 'qimei': '867905028376327',
        # 'Cookie': '&lskey=&luin=&skey=&uin=&kb_qbid=&qb_guid=e9234a46039624c2594ff227377988cb&qb_qua=QV=3&PL=ADR&PR=KB&PP=com.tencent.reading&PPVN=6.2.30.0&CO=SYS&PB=GE&VE=P&DE=PHONE&CHID=70307&LCID=0&MO= PRO5 &RL=1080*1920&OS=5.1&API=22&REF=qb_0&TM=00&logintype=0',
        # 'tu_openid': '01019D64DB848516AEDED6580107DCF1AFD1F472BD50DC0EBA10EF452D8942D3E1648DF5C584388D1B77B234',
        'chlid': '26134',
        # 'imsi_history': '0',
        # 'qn-sig': 'ce61cd1d81c44278842c61209203a560',
        # 'qn-rid': '1a8275d4-7182-4337-9e4f-7f387e19ce03',
        # 'hw_fp': 'Meizu/meizu_PRO5/PRO5:5.1/LMY47D/m86.Flyme_OS_5.1460690652:user/release-keys',
        # 'gpu': 'ARM Mali-T760',
        # 'mid': '403190a212c6457c45bc96f21ab7224cad2b864a',
        # 'devid': '867905028376327',
        # 'mac': '68:3E:34:9D:0C:CB',
        # 'store': '70307',
        # 'screen_height': '1920',
        'apptype': 'android',
        # 'origin_imei': '867905028376327',
        # 'codeclevel': '5.0',
        # 'rover': '1',
        # 'hw': 'Meizu_PRO5',
        # 'appversion': '6.2.30',
        'appver': '22_areading_6.2.30',
        # 'uid': 'ade3e6c263a1b00d',
        # 'screen_width': '1080',
        # 'sceneid': '',
        # 'android_id': 'ade3e6c263a1b00d'
    }

    response = requests.post('https://r.cnews.qq.com/getSubNewsIndex',params=params,
                             data=data)

    print(response.text)

def getSubNewsIndexNext():
    import requests

    cookies = {
        'lskey': '',
        'luin': '',
        'skey': '',
        'uin': '',
        'kb_qbid': '',
        'qb_guid': 'e9234a46039624c2594ff227377988cb',
        'qb_qua': 'QV=3&PL=ADR&PR=KB&PP=com.tencent.reading&PPVN=6.2.30.0&CO=SYS&PB=GE&VE=P&DE=PHONE&CHID=70307&LCID=0&MO= PRO5 &RL=1080*1920&OS=5.1&API=22&REF=qb_0&TM=00',
        'logintype': '0',
    }

    headers = {
        'Host': 'r.cnews.qq.com',
        'Referer': 'http://cnews.qq.com/cnews/android/',
        'User-Agent': '%E7%9C%8B%E7%82%B9%E5%BF%AB%E6%8A%A56230(android)',
        'snqn': '8KWbw+lUWdkUNym273cmvL5FOG4HOaLcvQlwHNoHKHij7Y8B/JfHqAlGfvMzVNvdfw5NPyKCuurdFXt1c6ZBzlhA6GPiGB7CxLUcfCpHAYk6YeEEDr0mrww4B5oYJyurtZYds5B4Ax/9g7br+lLIrA==',
        'svqn': '1_4',
        'qn-sig': 'd2f0a62b0e578738a456541a2048f0be',
        'qn-rid': '5d1f1296-4c33-4176-b36b-a819f2b6dcf9',
    }

    params = (
        ('devid', '867905028376327'),
    )

    data = {
        'cityList': '',
        'isUpdatingLocation': '1',
        'REQBuildTime': '1585202379754',
        'ssid': '<unknown ssid>',
        'omgid': '',
        'REQExecTime': '1585202379755',
        'qqnetwork': 'wifi',
        'commonsid': 'a389e0b410e249e6b99aff24e9780fc8',
        'kingCardType': '0',
        'picSizeMode': '0',
        'commonGray': '1_3|2_0|18_1|12_0|22_1|49_0|47_1|14_0|17_0|30_0|42_0|99_0',
        'currentTab': 'kuaibao',
        'proxy_addr': '172.30.6.19:8888',
        'is_wap': '0',
        'lastCheckCardType': '0',
        'omgbizid': '',
        'imsi': '',
        'commonIsFirstLaunch': '0',
        'chlidType': '0',
        'taid': '0101869F9CFE37D73B68DC94E0869278F6341C23C23AB3665B04598DAFED432764555F65EC4CF248F523DA5B',
        'ids': '20200326A0B76M00,20200326A0B6WZ00,20200326A0B78O00,20200326A0AHLD00,20200326A0AOI000,20200326A0AJCZ00,20200326A0AJCP00,20200326A0A5FD00,20200326A09Z4V00,20200326A09U4400,20200326A09RTL00,20200326A09RTC00,20200326A09GCC00,20200326A09GCB00,20200326A098PB00,20200326A098P900,20200326A08ZKM00,20200326A08WN700,20200326A08WN200,20200326A08M6200',
        'activefrom': 'icon',
        'unixtimesign': '1585202379757',
        'qimei': '867905028376327',
        'Cookie': '&lskey=&luin=&skey=&uin=&kb_qbid=&qb_guid=e9234a46039624c2594ff227377988cb&qb_qua=QV=3&PL=ADR&PR=KB&PP=com.tencent.reading&PPVN=6.2.30.0&CO=SYS&PB=GE&VE=P&DE=PHONE&CHID=70307&LCID=0&MO= PRO5 &RL=1080*1920&OS=5.1&API=22&REF=qb_0&TM=00&logintype=0',
        'tu_openid': '01019D64DB848516AEDED6580107DCF1AFD1F472BD50DC0EBA10EF452D8942D3E1648DF5C584388D1B77B234',
        'chlid': '26082',
        'imsi_history': '0',
        'qn-sig': 'd2f0a62b0e578738a456541a2048f0be',
        'qn-rid': '5d1f1296-4c33-4176-b36b-a819f2b6dcf9',
        'hw_fp': 'Meizu/meizu_PRO5/PRO5:5.1/LMY47D/m86.Flyme_OS_5.1460690652:user/release-keys',
        'gpu': 'ARM Mali-T760',
        'mid': '403190a212c6457c45bc96f21ab7224cad2b864a',
        'devid': '867905028376327',
        'mac': '68:3E:34:9D:0C:CB',
        'store': '70307',
        'screen_height': '1920',
        'apptype': 'android',
        'origin_imei': '867905028376327',
        'codeclevel': '5.0',
        'rover': '1',
        'hw': 'Meizu_PRO5',
        'appversion': '6.2.30',
        'appver': '22_areading_6.2.30',
        'uid': 'ade3e6c263a1b00d',
        'screen_width': '1080',
        'sceneid': '',
        'android_id': 'ade3e6c263a1b00d'
    }

    response = requests.post('https://r.cnews.qq.com/getSubNewsListItems', headers=headers, params=params,
                             cookies=cookies, data=data)

    print(response.text)

def getThreePager():
    import requests

    cookies = {
        'lskey': '',
        'luin': '',
        'skey': '',
        'uin': '',
        'kb_qbid': '',
        'qb_guid': 'e9234a46039624c2594ff227377988cb',
        'qb_qua': 'QV=3&PL=ADR&PR=KB&PP=com.tencent.reading&PPVN=6.2.30.0&CO=SYS&PB=GE&VE=P&DE=PHONE&CHID=70307&LCID=0&MO= PRO5 &RL=1080*1920&OS=5.1&API=22&REF=qb_0&TM=00',
        'logintype': '0',
    }

    headers = {
        'Host': 'r.cnews.qq.com',
        'Referer': 'http://cnews.qq.com/cnews/android/',
        'User-Agent': '%E7%9C%8B%E7%82%B9%E5%BF%AB%E6%8A%A56230(android)',
        'snqn': 'EonEtlgt3uKdYUDoMefofaBhgMO4vlkMiydEKrtjwhp9Uq9fY79lnoM+nyetETbDI1bB9DBb0+lNS3XvCbrA7HnqdG2NsBKT3p6QAP8Fxj2d9BR0yBBeK8UOj+QByMBoI+cCJbO4+R0G3+YubU1xyQ==',
        'svqn': '1_4',
        'qn-sig': '2b510ef02e02af58a78bd121e7eb4ae1',
        'qn-rid': '1cb3c1c0-89aa-482d-bd6b-4572a8c6a606',
    }

    params = (
        ('devid', '867905028376327'),
    )

    data = {
        # 'cityList': '',
        # 'isUpdatingLocation': '1',
        # 'REQBuildTime': '1585203264251',
        # 'ssid': '<unknown ssid>',
        # 'omgid': '',
        # 'REQExecTime': '1585203264251',
        # 'qqnetwork': 'wifi',
        # 'commonsid': 'a389e0b410e249e6b99aff24e9780fc8',
        # 'kingCardType': '0',
        # 'picSizeMode': '0',
        # 'commonGray': '1_3|2_0|18_1|12_0|22_1|49_0|47_1|14_0|17_0|30_0|42_0|99_0',
        # 'currentTab': 'kuaibao',
        # 'proxy_addr': '172.30.6.19:8888',
        # 'is_wap': '0',
        # 'lastCheckCardType': '0',
        # 'omgbizid': '',
        # 'imsi': '',
        # 'commonIsFirstLaunch': '0',
        # 'chlidType': '0',
        # 'taid': '0101869F9CFE37D73B68DC94E0869278F6341C23C23AB3665B04598DAFED432764555F65EC4CF248F523DA5B',
        'ids': '20200326A0K59L00,20200326A0K57H00,20200326A0JZHJ00,20200326A0JWVJ00,20200326A0JWTW00,20200326A0JU6H00,20200326A0JOKN00,20200326A0JOKD00,20200326A0JOJ300,20200326A0JOHF00,20200326A0JIR100,20200326A0JIO000,20200326A0JD6B00,20200326A0JD5C00,20200326A0JD1X00,20200326A0JA9A00,20200326A0JA8W00,20200326A0JA9200,20200326A0JA7T00,20200326A0J7GG00',
        # 'activefrom': 'icon',
        # 'unixtimesign': '1585203264254',
        # 'qimei': '867905028376327',
        # 'Cookie': '&lskey=&luin=&skey=&uin=&kb_qbid=&qb_guid=e9234a46039624c2594ff227377988cb&qb_qua=QV=3&PL=ADR&PR=KB&PP=com.tencent.reading&PPVN=6.2.30.0&CO=SYS&PB=GE&VE=P&DE=PHONE&CHID=70307&LCID=0&MO= PRO5 &RL=1080*1920&OS=5.1&API=22&REF=qb_0&TM=00&logintype=0',
        # 'tu_openid': '01019D64DB848516AEDED6580107DCF1AFD1F472BD50DC0EBA10EF452D8942D3E1648DF5C584388D1B77B234',
        'chlid': '26082',
        # 'imsi_history': '0',
        # 'qn-sig': '2b510ef02e02af58a78bd121e7eb4ae1',
        # 'qn-rid': '1cb3c1c0-89aa-482d-bd6b-4572a8c6a606',
        # 'hw_fp': 'Meizu/meizu_PRO5/PRO5:5.1/LMY47D/m86.Flyme_OS_5.1460690652:user/release-keys',
        # 'gpu': 'ARM Mali-T760',
        # 'mid': '403190a212c6457c45bc96f21ab7224cad2b864a',
        # 'devid': '867905028376327',
        # 'mac': '68:3E:34:9D:0C:CB',
        # 'store': '70307',
        # 'screen_height': '1920',
        'apptype': 'android',
        # 'origin_imei': '867905028376327',
        # 'codeclevel': '5.0',
        # 'rover': '1',
        # 'hw': 'Meizu_PRO5',
        # 'appversion': '6.2.30',
        'appver': '22_areading_6.2.30',
        # 'uid': 'ade3e6c263a1b00d',
        # 'screen_width': '1080',
        # 'sceneid': '',
        # 'android_id': 'ade3e6c263a1b00d'
    }

    response = requests.post('https://r.cnews.qq.com/getSubNewsListItems',  params=params,
                              data=data)


    print(response.text)

def get_page_content():
    import requests

    cookies = {
        'lskey': '',
        'luin': '',
        'skey': '',
        'uin': '',
        'kb_qbid': '',
        'qb_guid': 'e9234a46039624c2594ff227377988cb',
        'qb_qua': 'QV=3&PL=ADR&PR=KB&PP=com.tencent.reading&PPVN=6.2.30.0&CO=SYS&PB=GE&VE=P&DE=PHONE&CHID=70307&LCID=0&MO= PRO5 &RL=1080*1920&OS=5.1&API=22&REF=qb_0&TM=00',
        'logintype': '0',
    }

    headers = {
        'Host': 'r.cnews.qq.com',
        'referer': 'http://cnews.qq.com/cnews/android/',
        # 'user-agent': '%E7%9C%8B%E7%82%B9%E5%BF%AB%E6%8A%A56230(android)',
        # 'snqn': 'KfvKjusijfgDmJt9L3yqrl7vauF5fYiqKVW6X3k5jXciTwvN0rXITVk0ej1W5f4tQD6io+6mT1VddQqZn98nk3otRX2+gTOaHHciohfos+EXSsIua/G2hg8nf38vq3spBEm3pk1mWmDthJySPtO1ww==',
        # 'svqn': '1_4',
        # 'qn-sig': 'a2669fdba922bc6557072b36f68f1c16',
        # 'qn-rid': 'c647f1d9-065c-4e0a-9a43-8d850983af45',
        'content-type': 'application/x-www-form-urlencoded',
    }

    params = (
        ('devid', '867905028376327'),
    )

    # data = 'id=20200328A065EZ00&cf_chlid=26082&appver=22_areading_6.2.30&apptype=android'
    data = 'id=20200328A070ZG00&appver=22_areading_6.2.30'

    response = requests.post('https://r.cnews.qq.com/getSubNewsContent', headers=headers, params=params,
                              data=data)

    # print(response.url)
    # print(response.text)
    import json
    j_data = json.loads(response.text)
    text = j_data["content"]["text"]
    print(text)

def get_web_content():
    import requests

    headers = {
        'authority': 'kuaibao.qq.com',
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'accept': 'application/json, text/plain, */*',
        'sec-fetch-dest': 'empty',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'referer': 'https://kuaibao.qq.com/s/20200328A070ZG00?refer=kb_news&chlid=26134&atype=0',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'cookie': 'kb_h5_user_id=KBH5UserId_15851180816235448; pgv_pvid=3778507266',
    }

    params = (
        ('id', '20200328A070ZG00'),
        # ('openid', ''),
        # ('uin', 'null'),
        # ('ukey', 'ukey_157562266102361484'),
        ('style', 'json'),
    )

    response = requests.get('https://kuaibao.qq.com/getSubNewsContent', headers=headers, params=params)

    print(response.url)
    print(response.text)

# getSubNewsIndex()

# getThreePager()

# get_page_content()

get_web_content()