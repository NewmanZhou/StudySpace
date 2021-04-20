# -*- coding: utf-8 -*-
# @Time   : 2021/2/2 10:24 上午
# @Author : NewmanZhou
# @Desc : ==============================================
# Life is Short I Use Python!!!                      ===
# If this runs wrong,don't ask me,I don't know why;  ===
# If this runs right,thank god,and I don't know why. ===
# Maybe the answer,my friend,is blowing in the wind. ===
# ======================================================
# @Project : StudySpace
# @FileName: dark_during.py
# @Software: PyCharm
import re, time, json, requests
from FateadmApiClass import FateadmApi


def dark_trading_login_js():
    headers = {
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    }
    params = (
        ('mod', 'logging'),
        ('action', 'login'),
        ('infloat', 'yes'),
        ('frommessage', ''),
        ('inajax', '1'),
        ('ajaxtarget', 'messagelogin'),
    )

    response = requests.get('http://lfwpmgou2lz3jnt7mg3gorzkfnhnhgumbijn4ubossgs3wzsxkg6gvyd.onion/member.php',
                            headers=headers, params=params, proxies=proxies, verify=False)
    formhash = re.search('formhash"\s*value="(.*?)"', response.text).group(1)
    datahash = re.search("updateseccode\('(.*?)'", response.text).group(1)
    loginhash = re.search("loginhash=(.*?)\">", response.text).group(1)

    cookies = requests.utils.dict_from_cookiejar(response.cookies)
    headers = {
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36',
        'Accept': '*/*',
        'Referer': 'http://lfwpmgou2lz3jnt7mg3gorzkfnhnhgumbijn4ubossgs3wzsxkg6gvyd.onion/',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    }

    params = (
        ('mod', 'seccode'),
        ('action', 'update'),
        ('idhash', datahash),
        ('0.9282357491761555', ''),
        ('modid', 'member::logging'),
    )

    response = requests.get('http://lfwpmgou2lz3jnt7mg3gorzkfnhnhgumbijn4ubossgs3wzsxkg6gvyd.onion/misc.php',
                            headers=headers, params=params, cookies=cookies, proxies=proxies, verify=False)

    cookies_01 = requests.utils.dict_from_cookiejar(response.cookies)
    cookies["coVW_2132_lastact"] = cookies_01["coVW_2132_lastact"]
    update = re.search("update=(\d+)", response.text).group(1)
    # 验证码地址：
    # http://lfwpmgou2lz3jnt7mg3gorzkfnhnhgumbijn4ubossgs3wzsxkg6gvyd.onion/misc.php?mod=seccode&update=44659&idhash=cSASSqRKI7Ck
    bash_image_url = "http://lfwpmgou2lz3jnt7mg3gorzkfnhnhgumbijn4ubossgs3wzsxkg6gvyd.onion/misc.php?mod=seccode&update={}&idhash={}"
    imgUrl = bash_image_url.format(update, datahash)
    # 获取验证码
    headers = {
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36',
        'Accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
        'Referer': 'http://lfwpmgou2lz3jnt7mg3gorzkfnhnhgumbijn4ubossgs3wzsxkg6gvyd.onion/',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    }

    response = requests.get(imgUrl,
                            headers=headers, cookies=cookies, proxies=proxies, verify=False)

    cookies_02 = requests.utils.dict_from_cookiejar(response.cookies)
    cookies = Merge(cookies, cookies_02)
    with open('stading.png', 'wb') as f:
        for chunk in response.iter_content(chunk_size=32):
            f.write(chunk)
        f.close()
    yzm = TestFunc()
    cookies_base = {
        'coVW_2132_noticeTitle': '1',
        'coVW_2132_sendmail': '1', }
    cookies = Merge(cookies, cookies_base)
    headers = {
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'Upgrade-Insecure-Requests': '1',
        'Origin': 'http://lfwpmgou2lz3jnt7mg3gorzkfnhnhgumbijn4ubossgs3wzsxkg6gvyd.onion',
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Referer': 'http://lfwpmgou2lz3jnt7mg3gorzkfnhnhgumbijn4ubossgs3wzsxkg6gvyd.onion/',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    }

    params = (
        ('mod', 'logging'),
        ('action', 'login'),
        ('loginsubmit', 'yes'),
        ('handlekey', 'login'),
        ('loginhash', loginhash),
        ('inajax', '1'),
    )

    data = {
        'formhash': formhash,
        'referer': 'http://lfwpmgou2lz3jnt7mg3gorzkfnhnhgumbijn4ubossgs3wzsxkg6gvyd.onion/',
        'loginfield': 'username',
        'username': '611098',
        'password': 'qwerty123',
        'answer': '',
        'seccodehash': datahash,
        'seccodemodid': 'member::logging',
        'seccodeverify': yzm
    }

    response = requests.post('http://lfwpmgou2lz3jnt7mg3gorzkfnhnhgumbijn4ubossgs3wzsxkg6gvyd.onion/member.php',
                             headers=headers, params=params, cookies=cookies, proxies=proxies, data=data, verify=False)

    cookies_03 = requests.utils.dict_from_cookiejar(response.cookies)
    cookies_03["coVW_2132_lastvisit"] = cookies["coVW_2132_lastvisit"]
    cookies_03["coVW_2132_saltkey"] = cookies["coVW_2132_saltkey"]
    cookies_03["coVW_2132_noticeTitle"] = '1'
    cookies_03["coVW_2132_sendmail"] = '1'
    # 登录获取到返回的cookies中的 auth 后，还需要再次认证lip 认证通过后，
    # 才可以使用 auth + saltkey 拼装cookies 进行数据采集
    headers = {
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Referer': 'http://lfwpmgou2lz3jnt7mg3gorzkfnhnhgumbijn4ubossgs3wzsxkg6gvyd.onion/',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    }

    response = requests.get('http://lfwpmgou2lz3jnt7mg3gorzkfnhnhgumbijn4ubossgs3wzsxkg6gvyd.onion/', headers=headers,
                            cookies=cookies_03, proxies=proxies, verify=False)
    print(response.text)

    login_cookie = dict()
    login_cookie["coVW_2132_saltkey"] = cookies["coVW_2132_saltkey"]
    login_cookie["coVW_2132_auth"] = cookies_03["coVW_2132_auth"]
    print('\n')
    print(login_cookie)


def Merge(dict1, dict2):
    res = {**dict1, **dict2}
    return res


def getContent():
    import requests

    cookies = {'coVW_2132_saltkey': 'dOoLcPn5',
               'coVW_2132_auth': '19acy%2F4nmSRSnYZoqKY6BDMGybjI7LAI4AS6rXRWORNc4aHilIZXBfs2V4MUbLK7gfU%2BUSoLQcG9oYc%2FKKmtIEAoBg'}

    headers = {
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    }

    response = requests.get(
        'http://lfwpmgou2lz3jnt7mg3gorzkfnhnhgumbijn4ubossgs3wzsxkg6gvyd.onion/thread-75254-1-1.html', headers=headers,
        cookies=cookies, proxies=proxies, verify=False)

    print(response.text)


def TestFunc():
    pd_id = "127292"
    pd_key = "D+Wf6PwODfCUcjHf/hEDJetHae2QNxiX"
    app_id = "327292"
    app_key = "bsKzFtEaf7/5jZfI0aO5tTjf50gLY+/K"
    # 具体类型可以查看官方网站的价格页选择具体的类型，不清楚类型的，可以咨询客服
    pred_type = "20400"
    # 初始化api接口
    api = FateadmApi(app_id, app_key, pd_id, pd_key)
    # 查询余额接口
    # balance = api.QueryBalcExtend()  # 直接返余额
    # api.QueryBalc()

    # 通过文件识别验证码
    # 通过文件进行验证码识别,请使用自己的图片文件替换
    # 如果是通过url直接获取内存图片，这直接调用 Predict接口就好
    file_name = "stading.png"
    # res =  api.PredictFromFileExtend(pred_type,file_name)  	# 直接返回识别结果
    # 多网站类型时，需要增加src_url参数，具体请参考api文档: http://docs.fateadm.com/web/#/1?page_id=6
    rsp = api.PredictFromFile(pred_type, file_name)  # 返回识别结果的详细信息
    print(rsp)
    result = json.loads(rsp.get("RspData"))['result']
    return result


def getList():
    import requests

    cookies = {
        'coVW_2132_lastvisit': '1612675120',
        'coVW_2132_saltkey': 'leSSEeiE',
        'coVW_2132_seccodecSAnnqK66UNO': '194.9025ee0b9c0dd0226b',
        'coVW_2132_auth': '87fbr36aXMVfK7Tp75pEgUD5jsVNHusiZW265IFZMS%2FdQzDRi0DzygW8rwfpshfkbp72JAEc2qHjxwqmsaRr09umPg',
        'coVW_2132_lastcheckfeed': '38296%7C1612678851',
        'coVW_2132_nofavfid': '1',
        'coVW_2132_ignore_notice': '1',
        'coVW_2132_sid': 'bT48CA',
        'coVW_2132_lip': '127.0.0.1%2C1612774472',
        'coVW_2132_st_t': '38296%7C1612775747%7C2414776fa7fba22a9a0fcdc00b9bf490',
        'coVW_2132_forum_lastvisit': 'D_2_1612775747',
        'coVW_2132_ulastactivity': 'a9b48BrkoueGYMAssN3NljGvRGrZtdfJx7lsCgEGJBR6GdeyEt7v',
        'coVW_2132_sendmail': '1',
        'coVW_2132_noticeTitle': '1',
        'coVW_2132_lastact': '1612776004%09forum.php%09ajax',
    }

    headers = {
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    }

    response = requests.get('http://lfwpmgou2lz3jnt7mg3gorzkfnhnhgumbijn4ubossgs3wzsxkg6gvyd.onion/forum-2-1.html',
                            headers=headers, cookies=cookies, proxies=proxies, verify=False)
    print(response.status_code)
    print("\n")
    print(response.text)



if __name__ == '__main__':
    proxies = {
        'http': 'socks5h://localhost:9050',
        'https': 'socks5h://localhost:9050'
    }
    # dark_trading_login_js()
    # getContent()
    # ishaveAuth()
    getList()
    '''
    cf69248b cSAugYs95QD8 Lm2gx
    {'coVW_2132_lastact': '1612680342%09misc.php%09seccode',
     'coVW_2132_lastvisit': '1612676738', 
     'coVW_2132_saltkey': 'WgFmES88',
      'coVW_2132_sid': 's95QD8', 
      'coVW_2132_seccodecSAugYs95QD8': '273.e73686188c28118bcc'}
      
    登录获取auth  后返回的cookie：
    {'coVW_2132_auth': '4966aS02cU5TMho9IBugWqJCxMSA3IKmi5lX6jtufshnYfElilM8PrRUrXceghki1YFc3uBGfSo0a8OCCwBAN2Tujw', 
    'coVW_2132_checkfollow': '1', 
    'coVW_2132_lastact': '1612681152%09member.php%09logging', 
    'coVW_2132_lastcheckfeed': '38296%7C1612681152',
     'coVW_2132_lip': '127.0.0.1%2C1612679924', 
     'coVW_2132_sid': 'DqtNAd', 
     'coVW_2132_ulastactivity': 'cdb7IX6bV9tmFpvSiMRUQJBsE2sVv2%2BvVd5S2Hm3ElCPYjmUjQww'}
     
     
    '''
