# -*- coding: utf-8 -*-
# @Time   : 2020/3/4 4:44 下午
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

    cookies = {
        'wxuin': '1212006700',
        'devicetype': 'android-19',
        'version': '270004c9',
        'lang': 'zh_CN',
        'pass_ticket': 'U2b0cUj80PpZwWwaJzTijnIVSklr2DHPLnAlEVFxW0NWBEp524g6UbSuowrluYBO',
        'wap_sid2': 'CKyC98EEElxaRzl2UU9IeF9RNlVOel9kQVQ2Q19scEtjNGxBNTgyNlctTkVBTGdxSkw2dm5FbHJTU3R5Z0RoTzlVTXRzSjlIdGd1eHlHVDYtbmtZdm4xTWR0SGdDQnNFQUFBfjCf0f3yBTgNQJVO',
    }

    headers = {
        'Host': 'mp.weixin.qq.com',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 4.4.4; R8207 Build/KTU84P; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/67.0.3396.87 XWEB/1168 MMWEBSDK/190301 Mobile Safari/537.36 MMWEBID/8564 MicroMessenger/7.0.4.1420(0x270004C9) Process/toolsmp NetType/WIFI Language/zh_CN',
        'X-Requested-With': 'XMLHttpRequest',
        'Accept': '*/*',
        'Referer': 'https://mp.weixin.qq.com/mp/profile_ext?action=home&__biz=MzA5MzI3NjE2MA==&devicetype=android-19&version=270004c9&lang=zh_CN&nettype=WIFI&a8scene=7&session_us=gh_15d5aef889d8&pass_ticket=U2b0cUj80PpZwWwaJzTijnIVSklr2DHPLnAlEVFxW0NWBEp524g6UbSuowrluYBO&wx_header=1',
        'Accept-Language': 'zh-CN,en-US;q=0.9',
    }

    params = (
        ('action', 'getmsg'),
        ('__biz', 'MzA5MzI3NjE2MA=='),
        ('f', ['json', 'json']),
        ('offset', '10'),
        ('count', '10'),
        ('is_ok', '1'),
        ('scene', ''),
        ('uin', '777'),
        ('key', '777'),
        ('pass_ticket', 'U2b0cUj80PpZwWwaJzTijnIVSklr2DHPLnAlEVFxW0NWBEp524g6UbSuowrluYBO'),
        ('wxtoken', ''),
        ('appmsg_token', '1051_q5Cebw9Zuf9Itii1sYG-Jmyvxh2Yu42ZYms3ug~~'),
        ('x5', '0'),
    )

    response = requests.get('https://mp.weixin.qq.com/mp/profile_ext', headers=headers, params=params, cookies=cookies)

    print(response.text)


def getContent():
    import requests

    cookies = {
        'devicetype': 'android-19',
        'version': '270004c9',
        'lang': 'zh_CN',
    }

    headers = {
        'X-WECHAT-KEY': '98d573134dacceba55a54efdff2317ead3b1055483ef28858324b4dca0efcc8d469e24572fdfb7ef8580f07fc2db3673629361abc6615cd7c057f7c7429b32daf2f9efb6bf4aef1060a343ce2a12263a',
        'X-WECHAT-UIN': 'MTIxMjAwNjcwMA%3D%3D',
        'User-agent': 'Mozilla/5.0 (Linux; Android 4.4.4; R8207 Build/KTU84P; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/67.0.3396.87 XWEB/1168 MMWEBSDK/190301 Mobile Safari/537.36 MMWEBID/8564 MicroMessenger/7.0.4.1420(0x270004C9) Process/toolsmp NetType/WIFI Language/zh_CN MicroMessenger/7.0.4.1420(0x270004C9) Process/toolsmp NetType/WIFI Language/zh_CN',
        'Host': 'mp.weixin.qq.com',
    }

    params = (
        ('f', ['json', 'json', 'json']),
        ('mock', ''),
        ('fasttmplajax', '1'),
        ('uin', ''),
        ('key', ''),
        ('pass_ticket', ['U2b0cUj80PpZwWwaJzTijnIVSklr2DHPLnAlEVFxW0NWBEp524g6UbSuowrluYBO',
                         'U2b0cUj80PpZwWwaJzTijnIVSklr2DHPLnAlEVFxW0NWBEp524g6UbSuowrluYBO']),
        ('wxtoken', ''),
        ('devicetype', 'android-19'),
        ('clientversion', '270004c9'),
        ('__biz', 'MzA5MzI3NjE2MA=='),
        ('appmsg_token', ''),
        ('x5', '0'),
        ('wx_header', '1'),
    )

    data = {
        'r': '0.7814676257725806',
        '__biz': 'MzA5MzI3NjE2MA==',
        'appmsg_type': '9',
        'mid': '2650248369',
        'sn': 'b4eecaa830fbba075df05917eef72935',
        'idx': '1',
        'scene': '27',
        'title': '%E7%8E%B0%E5%9C%A8%EF%BC%8C%E6%88%91%E5%B7%B2%E7%BB%8F%E4%B8%8D%E5%86%8D%E6%81%90%E6%85%8C%E4%BA%86',
        'ct': '1580113012',
        'abtest_cookie': '',
        'devicetype': 'android-19',
        'version': '270004c9',
        'is_need_ticket': '0',
        'is_need_ad': '0',
        'comment_id': '1183141712810672128',
        'is_need_reward': '0',
        'both_ad': '0',
        'reward_uin_count': '0',
        'send_time': '',
        'msg_daily_idx': '1',
        'is_original': '0',
        'is_only_read': '1',
        'req_id': '',
        'pass_ticket': 'U2b0cUj80PpZwWwaJzTijnIVSklr2DHPLnAlEVFxW0NWBEp524g6UbSuowrluYBO',
        'is_temp_url': '0',
        'item_show_type': '0',
        'tmp_version': '1',
        'more_read_type': '0',
        'appmsg_like_type': '2',
        'related_video_sn': '',
        'vid': '',
        'is_pay_subscribe': '0',
        'pay_subscribe_uin_count': '0',
        'has_red_packet_cover': '0'
    }

    response = requests.post('https://mp.weixin.qq.com/mp/getappmsgext', headers=headers, params=params,
                             cookies=cookies, data=data)

    print(response.text)


# getList()
# getContent()

