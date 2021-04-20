# -*- coding: utf-8 -*-
import chardet
import requests, re, json, jsonpath


def kuaishouUserList():
    headers = {
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-User': '?1',
        'Sec-Fetch-Dest': 'document',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    }

    response = requests.get('https://live.kuaishou.com/profile/renminwang', headers=headers)
    res = re.search('window.__APOLLO_STATE__=\s?([\s\S]+?);\s?\(function', response.text)[1]
    dic_data = json.loads(res, strict=False)
    list = jsonpath.jsonpath(dic_data, "$..list")
    print(dic_data)
    # print(list)


def getSharlUrl():
    import requests

    cookies = {
        'clientid': '3',
        'did': 'web_37663519b71b295f41d501fb80888269',
        # 'client_key': '65890b29',
        # 'didv': '1594953285000',
        # 'kuaishou.live.bfb1s': '7206d814e5c089a58c910ed8bf52ace5',
        'Hm_lvt_86a27b7db2c5c0ae37fee4a8a35033ee': '1598321325',
        'Hm_lpvt_86a27b7db2c5c0ae37fee4a8a35033ee': '1598321325',
        'userId': '1417278167',
        'kuaishou.live.web_st': 'ChRrdWFpc2hvdS5saXZlLndlYi5zdBKgAQK5bNPV6JITU_nPpJnB2u7A-KeK1c8uZEKTLRZSLLewvwgnSlRaJyXwAd7RKJT9F48RuyQAKpDdrfsgXxgBGCf1igtkeSncwGDTQyTUX0soESYeDuFMu1eq2fu5EYpSGinMndmLauc8iOh1rQ0M2AJwJ-z8F0Z7AZIMPFIhTFcyf8yD9nDz9rbs-FhV8wnZzHfHqUfN4StBf3BOugHbR-gaEvsuz1ia_EwztqTXeP7HMv4rLSIgqRXhcZbe8djJwcFgW3AIbXBdsNc7D1S0EU7XbjDQ0ZsoBTAB',
        'kuaishou.live.web_ph': '85c9e1ca82f2dd1fc6a93313c4205fb82fa3',
    }

    headers = {
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'accept': '*/*',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36',
        'content-type': 'application/json',
        'Origin': 'https://live.kuaishou.com',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://live.kuaishou.com/profile/renminwang',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    }

    data = '{"operationName":"SharePageQuery","variables":{"photoId":"3xz792srxjxbtni","principalId":"renminwang"},"query":"query SharePageQuery($principalId: String, $photoId: String) {\\n feedById(principalId: $principalId, photoId: $photoId) {\\n currentWork {\\n playUrl\\n __typename\\n }\\n __typename\\n }\\n}\\n"}'

    response = requests.post('https://live.kuaishou.com/m_graphql', headers=headers, cookies=cookies, data=data)

    print(response.text)


def getNextPage():
    import requests

    cookies = {
        'clientid': '3',
        # 'did': 'web_37663519b71b295f41d501fb80888269',
        # 'client_key': '65890b29',
        # 'didv': '1594953285000',
        # 'kuaishou.live.bfb1s': '7206d814e5c089a58c910ed8bf52ace5',
        # 'Hm_lvt_86a27b7db2c5c0ae37fee4a8a35033ee': '1598321325',
        # 'Hm_lpvt_86a27b7db2c5c0ae37fee4a8a35033ee': '1598321325',
        'userId': '1417278167',
        # 'kuaishou.live.web_st': 'ChRrdWFpc2hvdS5saXZlLndlYi5zdBKgAQK5bNPV6JITU_nPpJnB2u7A-KeK1c8uZEKTLRZSLLewvwgnSlRaJyXwAd7RKJT9F48RuyQAKpDdrfsgXxgBGCf1igtkeSncwGDTQyTUX0soESYeDuFMu1eq2fu5EYpSGinMndmLauc8iOh1rQ0M2AJwJ-z8F0Z7AZIMPFIhTFcyf8yD9nDz9rbs-FhV8wnZzHfHqUfN4StBf3BOugHbR-gaEvsuz1ia_EwztqTXeP7HMv4rLSIgqRXhcZbe8djJwcFgW3AIbXBdsNc7D1S0EU7XbjDQ0ZsoBTAB',
        # 'kuaishou.live.web_ph': '85c9e1ca82f2dd1fc6a93313c4205fb82fa3',
    }

    headers = {
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'accept': '*/*',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36',
        'content-type': 'application/json',
        'Origin': 'https://live.kuaishou.com',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://live.kuaishou.com/profile/renminwang',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    }

    data = '{"operationName":"publicFeedsQuery","variables":{"principalId":"renminwang","pcursor":"1.597887572438E12","count":24},"query":"query publicFeedsQuery($principalId: String, $pcursor: String, $count: Int) {\\n publicFeeds(principalId: $principalId, pcursor: $pcursor, count: $count) {\\n pcursor\\n live {\\n user {\\n id\\n avatar\\n name\\n __typename\\n }\\n watchingCount\\n poster\\n coverUrl\\n caption\\n id\\n playUrls {\\n quality\\n url\\n __typename\\n }\\n quality\\n gameInfo {\\n category\\n name\\n pubgSurvival\\n type\\n kingHero\\n __typename\\n }\\n hasRedPack\\n liveGuess\\n expTag\\n __typename\\n }\\n list {\\n id\\n thumbnailUrl\\n poster\\n workType\\n type\\n useVideoPlayer\\n imgUrls\\n imgSizes\\n magicFace\\n musicName\\n caption\\n location\\n liked\\n onlyFollowerCanComment\\n relativeHeight\\n timestamp\\n width\\n height\\n counts {\\n displayView\\n displayLike\\n displayComment\\n __typename\\n }\\n user {\\n id\\n eid\\n name\\n avatar\\n __typename\\n }\\n expTag\\n __typename\\n }\\n __typename\\n }\\n}\\n"}'

    response = requests.post('https://live.kuaishou.com/m_graphql', headers=headers, cookies=cookies, data=data)

    j_data = json.loads(response.text)
    list_data = jsonpath.jsonpath(j_data, "$..list")[0]
    for ld in list_data:
        caption = ld.get("caption")
    print(j_data)


def getNoLogo():
    headers = {
        'Host': 'wxmini-api.uyouqu.com',
        'cookie': 'clientid=13;language=zh_C/N; brand=Meizu; sid=kuaishou.wechat.app; appId=ks_wechat_small_app_2; did=wxo_4db0bebb62207361e856b6e766fdc94bea7b; session_key=1230ea47a70bc4246e6354510ff9b10653331099f6685e918f3ec490a8cd529e825394ac358df0644cf742eb2b67f03f5fe71a120329d922ea3f4e91a87a3014fd7b1e7ace54222075c060ea5cd66cbb85231808aaea2f683982510b0d115594c4555a6b9dbb64d028053001; eUserStableOpenId=1230f1599d4c10ca535edc921fdf73cc525ad495f1fdc9822cc0f845a18d8b5ab5c3f17fce1fae8605770ef42a294a8d31241a1235445de99e354c4b9a1fa7bd1e00a2e6624f22205c1fc0e3d1adcadc9e364e24e3dda42d8458895f5024faf79b95cf989992a40b28053001;',
        # 'cookie': 'clientid=13; ',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 5.1; PRO 5 Build/LMY47D) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.116 Mobile Safari/537.36 MicroMessenger/7.0.18.1740(0x27001235) Process/appbrand0 WeChat/arm64 NetType/WIFI Language/zh_CN ABI/arm64',
        'charset': 'utf-8',
        'content-type': 'application/json',
        'Referer': 'https://servicewechat.com/wx79a83b1a1e8a7978/266/page-frame.html',
    }
    data = '{"count":24,"eid":"974889968","pcursor":"1.59789471584E12"}'
    # data = '{"count":24,"eid":"974889968"}'

    response = requests.post('https://wxmini-api.uyouqu.com/rest/wd/wechatApp/feed/profile', headers=headers, data=data)

    print(response.text)


def yidiantong():
    headers = {
        # 'x-ac-token-ticket': '',
        # 'x-ac-device-id': '3c6a82afed1e7b32',
        'Accept': 'application/json',
        'x-ac-os-info': 'Android',
        # 'anonymousId': '3c6a82afed1e7b32',
        'Referer': 'https://ecustomer.cntaiping.com/',
        # 'x-ac-app-version': '',
        'Content-Type': 'application/json; charset=UTF-8',
        'Host': 'ecustomer.cntaiping.com',
        'User-Agent': 'okhttp/3.11.0',
    }

    params = (
        ('language', 'zh-cn'),
    )

    data = '{"id":"2","pageNo":1,"pageSize":10}'

    response = requests.post('https://ecustomer.cntaiping.com/campaignsms/essay/queryEssayListV3', headers=headers,
                             data=data)

    print(response.text)


def xigua():
    cookies = {
        'ttwid': '6894473280901989892',
        'ttwid.sig': 'M7d34SseuHwbd2OKyVyVQEg8vrg',
        'xiguavideopcwebid': '6894473280901989892',
        'xiguavideopcwebid.sig': 'B7mOR0X8Nd2I1i3JtdCvLNqwGog',
        'Hm_lvt_db8ae92f7b33b6596893cdf8c004a1a2': '1605244659',
        'MONITOR_WEB_ID': '27310ce3-61b8-4057-a5e6-f3c62b125484',
        '_ga': 'GA1.2.1338572706.1605244660',
        '_gid': 'GA1.2.80726669.1605244660',
        'ixigua-a-s': '1',
        'Hm_lpvt_db8ae92f7b33b6596893cdf8c004a1a2': '1605247093',
    }

    headers = {
        'Host': 'www.ixigua.com',
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'accept': 'application/json, text/plain, */*',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://www.ixigua.com/home/55288942499',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
    }

    params = (
        # ('_signature', '_02B4Z6wo00f014OXgqQAAIBD8fu7wZUOy7eDloYAAL9X00'),
        ('author_id', '55288942499'),
        ('type', 'video'),
        ('max_time', '0'),
    )

    response = requests.get('https://www.ixigua.com/api/videov2/author/video', headers=headers, params=params,
                            )
    print(response.text)


def weixinxcx():
    import requests

    headers = {
        'Host': 'api.nicetuan.net',
        'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJ1aWQiOiIxMjIyMjQ4NjMiLCJuYmYiOjE2MDkyMDk4NjYsInVubSI6IldONjZSQ1FQTk02Tk9kRHFuYzZPb0QvRGdnZ2JNU3owS3VqKy9xeFVtYm89IiwiaXNzIjoieWhkeCIsImV4cCI6MTYwOTcyODI2NiwiaWF0IjoxNjA5MjA5ODY2LCJqdGkiOiI4Y2QxZTY5ODAyY2Q0MDhlYjQ1ZjcwMTRhZTJiYzdkZSJ9.7wjvS6J-U0fJD6cYvDHUwzFvL7v_QAr9vIr4s1FhxcDoj65oNaj60wUMHibB2jmFvoGomYZd6pYsq4tViAa-Sw',
        'charset': 'utf-8',
        'ver': '2.48.2',
        'x-tingyun': 'c=B|mLAIBDGzzNE',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 8.1.0; Pixel XL Build/OPM4.171019.021.P1; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/61.0.3163.98 Mobile Safari/537.36 MicroMessenger/7.0.22.1820(0x27001637) Process/appbrand0 WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64 MiniProgramEnv/android',
        'content-type': 'application/json',
        'source': 'weapp',
        'Referer': 'https://servicewechat.com/wxbbdca62c011eeb38/310/page-frame.html',
    }

    data = '{"categoryId":"746","grouponId":98768,"partnerId":696120,"p":1,"size":20}'

    response = requests.post('https://api.nicetuan.net/mc/diamondV2/list-by-category', headers=headers, data=data)
    print(response.text)


def china_blog():
    import requests

    # cookies = {
    #     'coob': '5085',
    #     'random': '1064',
    #     'PHPSESSID': 'rj80ehdin5ro1tjajv6cdaisqv',
    # }
    proxies = {
        'http': 'socks5h://localhost:9050',
        'https': 'socks5h://localhost:9050'
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:78.0) Gecko/20100101 Firefox/78.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
    }

    response = requests.get('http://xxxxxxxx3a3kuuhhw5w7stk25fzhttrlpiomij5bogkg7yyqsng5tqyd.onion/entrance/login.php',
                            headers=headers, proxies=proxies)

    print(response.status_code)
    print(response.headers)
    print("===" * 10)
    return_cookies = requests.utils.dict_from_cookiejar(response.cookies)
    return return_cookies.get('PHPSESSID', '')


def china_blog_dcss(PHPSESSID):
    import requests

    cookies = {
        'PHPSESSID': PHPSESSID,
        'userid': '611098',
    }
    proxies = {
        'http': 'socks5h://localhost:9050',
        'https': 'socks5h://localhost:9050'
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:78.0) Gecko/20100101 Firefox/78.0',
        'Accept': 'text/css,*/*;q=0.1',
        'Accept-Language': 'en-US,en;q=0.5',
        'Referer': 'http://xxxxxxxx3a3kuuhhw5w7stk25fzhttrlpiomij5bogkg7yyqsng5tqyd.onion/entrance/login.php',
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
    }

    response = requests.get('http://xxxxxxxx3a3kuuhhw5w7stk25fzhttrlpiomij5bogkg7yyqsng5tqyd.onion/images/d.css',
                            headers=headers, cookies=cookies, proxies=proxies)
    print(response.cookies)


def china_blog_pic(PHPSESSID):
    import requests

    cookies = {
        'coob': '5085',
        'random': '1064',
        'PHPSESSID': PHPSESSID,
    }
    print(cookies)
    proxies = {
        'http': 'socks5h://localhost:9050',
        'https': 'socks5h://localhost:9050'
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:78.0) Gecko/20100101 Firefox/78.0',
        'Accept': 'image/webp,*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Referer': 'http://xxxxxxxx3a3kuuhhw5w7stk25fzhttrlpiomij5bogkg7yyqsng5tqyd.onion/',
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
    }
    response = requests.get('http://xxxxxxxx3a3kuuhhw5w7stk25fzhttrlpiomij5bogkg7yyqsng5tqyd.onion/entrance/code76.php',
                            headers=headers, cookies=cookies, stream=True, proxies=proxies)

    print(response.status_code)
    with open('img.png', 'wb') as f:
        for chunk in response.iter_content(chunk_size=32):
            f.write(chunk)


def china_blog_stylecss(PHPSESSID):
    import requests

    cookies = {
        'PHPSESSID': PHPSESSID,
        'userid': '611098',
    }
    proxies = {
        'http': 'socks5h://localhost:9050',
        'https': 'socks5h://localhost:9050'
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:78.0) Gecko/20100101 Firefox/78.0',
        'Accept': 'text/css,*/*;q=0.1',
        'Accept-Language': 'en-US,en;q=0.5',
        'Referer': 'http://xxxxxxxx3a3kuuhhw5w7stk25fzhttrlpiomij5bogkg7yyqsng5tqyd.onion/entrance/login.php',
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
    }

    response = requests.get('http://xxxxxxxx3a3kuuhhw5w7stk25fzhttrlpiomij5bogkg7yyqsng5tqyd.onion/images/style.css',
                            headers=headers, cookies=cookies, proxies=proxies)
    print(response.status_code)


def china_blog_favicon(PHPSESSID):
    import requests

    cookies = {
        'PHPSESSID': PHPSESSID,
        'userid': '611098',
    }
    proxies = {
        'http': 'socks5h://localhost:9050',
        'https': 'socks5h://localhost:9050'
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:78.0) Gecko/20100101 Firefox/78.0',
        'Accept': 'image/webp,*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
    }

    response = requests.get('http://xxxxxxxx3a3kuuhhw5w7stk25fzhttrlpiomij5bogkg7yyqsng5tqyd.onion/favicon.ico',
                            headers=headers, cookies=cookies, proxies=proxies)

    print(response.status_code)


def china_blog_post_login(PHPSESSID, sub_code):
    import requests

    cookies = {
        'coob': '5085',
        'random': '1064',
        'PHPSESSID': PHPSESSID,
        'userid': '0',
    }
    proxies = {
        'http': 'socks5h://localhost:9050',
        'https': 'socks5h://localhost:9050'
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:78.0) Gecko/20100101 Firefox/78.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Referer': 'http://xxxxxxxx3a3kuuhhw5w7stk25fzhttrlpiomij5bogkg7yyqsng5tqyd.onion/entrance/login.php',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'http://xxxxxxxx3a3kuuhhw5w7stk25fzhttrlpiomij5bogkg7yyqsng5tqyd.onion',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
    }

    data = {
        'lgid': '611098',
        'lgpass': 'qwerty123',
        'sub_code': sub_code,
        'lgsub': '\u8FDB\u5165\u7CFB\u7EDF'
    }

    response = requests.get(
        'http://xxxxxxxx3a3kuuhhw5w7stk25fzhttrlpiomij5bogkg7yyqsng5tqyd.onion/entrance/logins.php', headers=headers,
        cookies=cookies, data=data, proxies=proxies)
    print(response.status_code)
    print(response.text)


def china_blog_get_logined(PHPSESSID, userid):
    import requests

    cookies = {
        'PHPSESSID': PHPSESSID,
        'userid': userid,
    }
    proxies = {
        'http': 'socks5h://localhost:9050',
        'https': 'socks5h://localhost:9050'
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:78.0) Gecko/20100101 Firefox/78.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Referer': 'http://xxxxxxxx3a3kuuhhw5w7stk25fzhttrlpiomij5bogkg7yyqsng5tqyd.onion/entrance/login.php',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
    }

    response = requests.get('http://xxxxxxxx3a3kuuhhw5w7stk25fzhttrlpiomij5bogkg7yyqsng5tqyd.onion/index.php',
                            headers=headers, cookies=cookies, proxies=proxies)

    print(response.status_code)
    print(response.text)


def china_blog_list_pager():
    import requests

    cookies = {
        'PHPSESSID': 'h5q94gos5a9f85dqi9m7976crn',
        'userid': '611098',
    }
    proxies = {
        'http': 'socks5h://localhost:9050',
        'https': 'socks5h://localhost:9050'
    }

    headers = {
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Referer': 'http://xxxxxxxx3a3kuuhhw5w7stk25fzhttrlpiomij5bogkg7yyqsng5tqyd.onion/ea.php?ea=10001&pagea=2',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    }

    params = (
        ('ea', '10001'),
        ('pagea', '1'),
    )

    response = requests.get('http://xxxxxxxx3a3kuuhhw5w7stk25fzhttrlpiomij5bogkg7yyqsng5tqyd.onion/ea.php',
                            headers=headers, params=params, cookies=cookies, proxies=proxies, verify=False)

    print(response.text)


def testSeleniumTor():
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    import time
    profile = Options()
    profile.add_argument('--proxy-server=127.0.0.1:9050')
    browser = webdriver.Chrome(options=profile)
    res = browser.get("http://xxxxxxxx3a3kuuhhw5w7stk25fzhttrlpiomij5bogkg7yyqsng5tqyd.onion")
    # res = browser.get("https://blog.csdn.net/xpt211314/article/details/103301344")
    print(res)
    # browser.save_screenshot("screenshot.png")
    # browser.close()


def testTor():
    import requests

    proxies = {
        'http': 'socks5h://localhost:9050',
        'https': 'socks5h://localhost:9050'
    }
    url = 'http://sblib3fk2gryb46d.onion'

    print(requests.get(url, proxies=proxies).text)


def ipaddresses():
    import binascii
    import ipaddress

    ADDRESSES = [
        '10.9.0.6',
        'fdfd:87b5:b475:5e3e:b1bc:e121:a8eb:14aa',
    ]

    for ip in ADDRESSES:
        addr = ipaddress.ip_address(ip)
        print(type(addr))
        print('{!r}'.format(addr))
        print('   IP version:', addr.version)
        print('   is private:', addr.is_private)
        print('  packed form:', binascii.hexlify(addr.packed))
        print('      integer:', int(addr))
        print()


def re_cookie():
    response = [{'name': 'userid', 'value': '611098',
                 'domain': 'xxxxxxxx3a3kuuhhw5w7stk25fzhttrlpiomij5bogkg7yyqsng5tqyd.onion', 'path': '/',
                 'expires': 1611059988.071822, 'size': 12, 'httpOnly': False, 'secure': False, 'session': False},
                {'name': 'PHPSESSID', 'value': 'iumnntu14h5vquhfmau456u5o0',
                 'domain': 'xxxxxxxx3a3kuuhhw5w7stk25fzhttrlpiomij5bogkg7yyqsng5tqyd.onion', 'path': '/', 'expires': -1,
                 'size': 35, 'httpOnly': True, 'secure': False, 'session': True}, {'name': 'random', 'value': '1064',
                                                                                   'domain': 'xxxxxxxx3a3kuuhhw5w7stk25fzhttrlpiomij5bogkg7yyqsng5tqyd.onion',
                                                                                   'path': '/', 'expires': -1,
                                                                                   'size': 10, 'httpOnly': False,
                                                                                   'secure': False, 'session': True}]
    str_response = str(response)
    res = re.findall("'PHPSESSID',\s+'value':\s+'(.*?)'", str_response)[0]
    print(res)


def postYUSHUANG():
    import requests

    headers = {
        'authority': 'like.threatbook-inc.cn',
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
        'content-type': 'application/json',
        'accept': '*/*',
        'origin': 'https://like.threatbook-inc.cn',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://like.threatbook-inc.cn/',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
        # 'cookie': 'gr_user_id=4409f85d-9b2e-488a-986e-7054166b56c3; 889930cec4eb8153_gr_session_id=66e5a131-8af4-454c-a0bf-aece263ea875; grwng_uid=6227af05-de63-4d4b-90a3-94af800d18f4; 889930cec4eb8153_gr_session_id_66e5a131-8af4-454c-a0bf-aece263ea875=true; user=eyJwYXNzcG9ydCI6eyJ1c2VyIjoiemhvdWppYW4ifSwiX2V4cGlyZSI6MTYxMTE0NDQ4MzUxNywiX21heEFnZSI6ODY0MDAwMDB9; user.sig=bHWyyDJX6azzsXGjIURSbLVRhZ8',
        'cookie': 'gr_user_id=00; grwng_uid=00; user=00; user.sig=00',
    }

    data = '{"toUser":"yushuang","info":"testtesttesttesttest"}'

    response = requests.post('https://like.threatbook-inc.cn/addPraise', headers=headers, data=data)
    print(response.status_code)


def dark_trading():
    import requests

    cookies = {
        'coVW_2132_lastvisit': '1611302969',
        'coVW_2132_saltkey': 'AavvhhjW',
        'coVW_2132_seccodecSAy16DwR5We': '556.997d24a178a4706525',
        'coVW_2132_seccodecSAOnJd1d3K9': '560.6558df2c70779b1585',
        'coVW_2132_seccodecSAQe7RnALwz': '610.74e66b29daed2f1d82',
        'coVW_2132_seccodecSAcbTxmcY69': '647.e90b1c948eb460f414',
        'coVW_2132_st_p': '0%7C1611308448%7C08039758f528069645802dcf18a8bf56',
        'coVW_2132_sendmail': '1',
        'coVW_2132_sid': 'z6zLQ0',
        'coVW_2132_lastact': '1611309015%09misc.php%09seccode',
    }

    headers = {
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36',
        'Accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
        'Referer': 'http://lfwpmgou2lz3jnt7mg3gorzkfnhnhgumbijn4ubossgs3wzsxkg6gvyd.onion/thread-4553-1-1.html',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    }

    params = (
        ('mod', 'seccode'),
        ('update', '18681'),
        ('idhash', 'cSAJ2rL26Qqd'),
    )

    response = requests.get('http://lfwpmgou2lz3jnt7mg3gorzkfnhnhgumbijn4ubossgs3wzsxkg6gvyd.onion/misc.php',
                            headers=headers, params=params, cookies=cookies, proxies=proxies, verify=False)

    print(response.status_code)
    print(response.text)
    with open('stading.png', 'wb') as f:
        for chunk in response.iter_content(chunk_size=32):
            f.write(chunk)
        f.close()
    # NB. Original query string below. It seems impossible to parse and
    # reproduce query strings 100% accurately so the one below is given
    # in case the reproduced version is not "correct".
    # response = requests.get('http://lfwpmgou2lz3jnt7mg3gorzkfnhnhgumbijn4ubossgs3wzsxkg6gvyd.onion/misc.php?mod=seccode&update=18681&idhash=cSAJ2rL26Qqd', headers=headers, cookies=cookies, verify=False)


def dark_trading_login():
    import requests

    cookies = {
        'coVW_2132_lastvisit': '1612158459',
        'coVW_2132_saltkey': 'bMY96g5Y',
        'coVW_2132_seccodecSAZEvvIwJXs': '180.6058161159424353a6',
        'coVW_2132_seccodecSAOGXfTzmc9': '188.e1cd716b4a91d83755',
        'coVW_2132_seccodecSALDgno4O3J': '695.b8016eded6ab8e21b4',
        'coVW_2132_seccodecSAA3TjCKIrg': '984.dacfaa3fc42f150d81',
        'coVW_2132_seccodecSAep3tZ5RjF': '991.9be00b3b49b1897a99',
        'coVW_2132_st_p': '0%7C1612179050%7C772df2e42eab39829dd7b73a52207f68',
        'coVW_2132_sid': 'i43c08',
        'coVW_2132_seccodecSACtQy4ndDW': '1031.1bb074e01ed440c31e',
        'coVW_2132_lastact': '1612179312%09misc.php%09seccode',
    }

    headers = {
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'Upgrade-Insecure-Requests': '1',
        'Origin': 'http://lfwpmgou2lz3jnt7mg3gorzkfnhnhgumbijn4ubossgs3wzsxkg6gvyd.onion',
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Referer': 'http://lfwpmgou2lz3jnt7mg3gorzkfnhnhgumbijn4ubossgs3wzsxkg6gvyd.onion/thread-75100-1-1.html',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    }

    params = (
        ('mod', 'logging'),
        ('action', 'login'),
        ('loginsubmit', 'yes'),
        ('frommessage', ''),
        ('loginhash', 'LoJ70'),
        ('inajax', '1'),
    )

    data = {
        'formhash': 'ccaa751c',
        'referer': 'http://lfwpmgou2lz3jnt7mg3gorzkfnhnhgumbijn4ubossgs3wzsxkg6gvyd.onion/thread-75100-1-1.html',
        'loginfield': 'username',
        'username': '611098',
        'password': 'qwerty123',
        'answer': '',
        'seccodehash': 'cSAy03F9r88C',
        'seccodemodid': 'member::logging',
        'seccodeverify': 'e9tf'
    }

    response = requests.post('http://lfwpmgou2lz3jnt7mg3gorzkfnhnhgumbijn4ubossgs3wzsxkg6gvyd.onion/member.php',
                             headers=headers, params=params, data=data, proxies=proxies, verify=False)
    print(response.status_code)
    print(requests.utils.dict_from_cookiejar(response.cookies))
    # NB. Original query string below. It seems impossible to parse and
    # reproduce query strings 100% accurately so the one below is given
    # in case the reproduced version is not "correct".
    # response = requests.post('http://lfwpmgou2lz3jnt7mg3gorzkfnhnhgumbijn4ubossgs3wzsxkg6gvyd.onion/member.php?mod=logging&action=login&loginsubmit=yes&frommessage&loginhash=LoJ70&inajax=1', headers=headers, cookies=cookies, data=data, verify=False)


def dark_trading_getList():
    import requests

    cookies = {
        'coVW_2132_lastvisit': '1612158459',
        'coVW_2132_saltkey': 'bMY96g5Y',
        'coVW_2132_seccodecSAZEvvIwJXs': '180.6058161159424353a6',
        'coVW_2132_seccodecSAOGXfTzmc9': '188.e1cd716b4a91d83755',
        'coVW_2132_seccodecSALDgno4O3J': '695.b8016eded6ab8e21b4',
        'coVW_2132_seccodecSAA3TjCKIrg': '984.dacfaa3fc42f150d81',
        'coVW_2132_seccodecSAep3tZ5RjF': '991.9be00b3b49b1897a99',
        'coVW_2132_seccodecSACtQy4ndDW': '1031.1bb074e01ed440c31e',
        'coVW_2132_ulastactivity': '2ea6DI59tAC2YT6nMrOEvCEL6HrQ1CkFApMt5N2Ebe5EC1PgS8Ku',
        'coVW_2132_auth': 'ef87L%2FrxUJwXcIJKxSuut0Gl2%2F0TBnqSadJaK7ogzUysOJeqDONNbOU%2BGbFTtGsPz%2Bfl9bA4LJexH4L73uI8NRcIUg',
        'coVW_2132_lastcheckfeed': '38296%7C1612179320',
        'coVW_2132_st_p': '38296%7C1612179326%7C4cd9db5d2996fa79d7f45d0322134c75',
        'coVW_2132_viewid': 'tid_75100',
        'coVW_2132_sid': 'D51n32',
        'coVW_2132_lip': '127.0.0.1%2C1612180262',
        'coVW_2132_nofavfid': '1',
        'coVW_2132_checkpm': '1',
        'coVW_2132_lastact': '1612180282%09home.php%09misc',
        'coVW_2132_sendmail': '1',
        'coVW_2132_noticeTitle': '1',
    }

    headers = {
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Referer': 'http://lfwpmgou2lz3jnt7mg3gorzkfnhnhgumbijn4ubossgs3wzsxkg6gvyd.onion/forum.php',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    }

    response = requests.get('http://lfwpmgou2lz3jnt7mg3gorzkfnhnhgumbijn4ubossgs3wzsxkg6gvyd.onion/forum-2-3.html',
                            headers=headers, proxies=proxies, verify=False)

    print(response.status_code)
    print(response.text)


def dark_during_content():
    import requests

    # cookies = {
    #     'coVW_2132_lastvisit': '1612158459',
    #     'coVW_2132_saltkey': 'bMY96g5Y',
    #     'coVW_2132_seccodecSAZEvvIwJXs': '180.6058161159424353a6',
    #     'coVW_2132_seccodecSAOGXfTzmc9': '188.e1cd716b4a91d83755',
    #     'coVW_2132_seccodecSALDgno4O3J': '695.b8016eded6ab8e21b4',
    #     'coVW_2132_seccodecSAA3TjCKIrg': '984.dacfaa3fc42f150d81',
    #     'coVW_2132_seccodecSAep3tZ5RjF': '991.9be00b3b49b1897a99',
    #     'coVW_2132_seccodecSACtQy4ndDW': '1031.1bb074e01ed440c31e',
    #     'coVW_2132_ulastactivity': '2ea6DI59tAC2YT6nMrOEvCEL6HrQ1CkFApMt5N2Ebe5EC1PgS8Ku',
    #     'coVW_2132_auth': 'ef87L%2FrxUJwXcIJKxSuut0Gl2%2F0TBnqSadJaK7ogzUysOJeqDONNbOU%2BGbFTtGsPz%2Bfl9bA4LJexH4L73uI8NRcIUg',
    #     'coVW_2132_lastcheckfeed': '38296%7C1612179320',
    #     'coVW_2132_st_p': '38296%7C1612179326%7C4cd9db5d2996fa79d7f45d0322134c75',
    #     'coVW_2132_viewid': 'tid_75100',
    #     'coVW_2132_sid': 'D51n32',
    #     'coVW_2132_lip': '127.0.0.1%2C1612180262',
    #     'coVW_2132_nofavfid': '1',
    #     'coVW_2132_noticeTitle': '1',
    #     'coVW_2132_st_t': '38296%7C1612180558%7C6735f46d4cc8bf6138b73e99efcf2647',
    #     'coVW_2132_forum_lastvisit': 'D_2_1612180558',
    #     'coVW_2132_lastact': '1612180637%09forum.php%09ajax',
    # }

    cookies = {
        # 'coVW_2132_lastvisit': '1612158459',
        'coVW_2132_saltkey': 'EdBa8dAO',
        # 'coVW_2132_seccodecSAZEvvIwJXs': '180.6058161159424353a6',
        # 'coVW_2132_seccodecSAOGXfTzmc9': '188.e1cd716b4a91d83755',
        # 'coVW_2132_seccodecSALDgno4O3J': '695.b8016eded6ab8e21b4',
        # 'coVW_2132_seccodecSAA3TjCKIrg': '984.dacfaa3fc42f150d81',
        # 'coVW_2132_seccodecSAep3tZ5RjF': '991.9be00b3b49b1897a99',
        # 'coVW_2132_seccodecSACtQy4ndDW': '1031.1bb074e01ed440c31e',
        # 'coVW_2132_ulastactivity': '2ea6DI59tAC2YT6nMrOEvCEL6HrQ1CkFApMt5N2Ebe5EC1PgS8Ku',
        'coVW_2132_auth': 'a638u0o2VWcrllY%2B1cKrfqQbXIz6A4O5yVoZTUI%2Br4Iqjj55qu40fZXBYgdBXzCsucAqZG3PNAhe%2F3OmtYkBOsMm9A',
        # 'coVW_2132_lastcheckfeed': '38296%7C1612179320',
        # 'coVW_2132_st_p': '38296%7C1612179326%7C4cd9db5d2996fa79d7f45d0322134c75',
        # 'coVW_2132_viewid': 'tid_75100',
        # 'coVW_2132_sid': 'D51n32',
        # 'coVW_2132_lip': '127.0.0.1%2C1612180262',
        # 'coVW_2132_nofavfid': '1',
        # 'coVW_2132_checkpm': '1',
        # 'coVW_2132_lastact': '1612180282%09home.php%09misc',
        # 'coVW_2132_sendmail': '1',
        # 'coVW_2132_noticeTitle': '1',
    }
    headers = {
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Referer': 'http://lfwpmgou2lz3jnt7mg3gorzkfnhnhgumbijn4ubossgs3wzsxkg6gvyd.onion/forum-2-3.html',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    }

    response = requests.get(
        'http://lfwpmgou2lz3jnt7mg3gorzkfnhnhgumbijn4ubossgs3wzsxkg6gvyd.onion/thread-75202-1-3.html', headers=headers,
        cookies=cookies,
        proxies=proxies, verify=False)

    print(response.status_code)
    print(response.text)


def scrapysplash():
    from scrapy.selector import Selector

    splash_url = 'http://localhost:8050/render.html'

    args = {'url': 'http://quotes.toscrape.com/js', 'timeout': 10, 'image': 0}

    response = requests.get(splash_url, params=args)

    sel = Selector(response)
    print(sel)

    data = sel.css('div.quote span.text::text').extract()
    print(data)


if __name__ == '__main__':
    proxies = {
        'http': 'socks5h://localhost:9050',
        'https': 'socks5h://localhost:9050'
    }

    # PHPSESSID = china_blog(
    # china_blog_stylecss(PHPSESSID)
    # china_blog_dcss(PHPSESSID)
    # china_blog_pic(PHPSESSID)
    #
    # china_blog_favicon(PHPSESSID)
    # print('==' * 15)
    # print(PHPSESSID)
    # china_blog_post_login("373odvgbvat9djma61ja8ms8gm", "733a")
    # china_blog_get_logined("rdfkjlgb3oj5cmcepo79l51lcg", "607271")
    # testSeleniumTor()
    # china_blog_list_pager()

    # re_cookie()
    # dark_trading_login()
    # dark_trading_getList()
    # dark_during_content()
    # scrapysplash()

