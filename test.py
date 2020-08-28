# -*- coding: utf-8 -*-
import chardet
import requests,re,json,jsonpath

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
    res = re.search('window.__APOLLO_STATE__=\s?([\s\S]+?);\s?\(function',response.text)[1]
    dic_data = json.loads(res, strict=False)
    list = jsonpath.jsonpath(dic_data,"$..list")
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
    list_data = jsonpath.jsonpath(j_data,"$..list")[0]
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

if __name__ == '__main__':
    getNoLogo()

    '''
    https://live.kuaishou.com/m_graphql
    
    https://txmov2.a.yximgs.com/upic/2020/08/24/17/BMjAyMDA4MjQxNzI1NDNfMTQxNzMyODYzXzM0OTIyMjcyNDg1XzFfMw==_b_B94b28ee6fb680239e57266a651ca772c.mp4
    
    https://jsmov2.a.yximgs.com/upic/2020/08/23/11/BMjAyMDA4MjMxMTQ2MTlfMTE0MTI5NDA0OF8zNDg0MjM5MTE5Ml8xXzM=_b_B5236352ab9f7d3b36519a6376904c881.mp4
    https://jsmov2.a.yximgs.com/upic/2020/08/24/20/BMjAyMDA4MjQyMDIzNTVfOTc0ODg5OTY4XzM0OTM0NjgyMTUyXzFfMw==_b_B1e730e5334a949b69800a505d57a41c3.mp4
    https://txmov2.a.yximgs.com/bs2/newWatermark/MzQ2NTk3ODMwMjc_zh_4.mp4"
    
    http://txmov2.a.yximgs.com/bs2/newWatermark/MzQ5MzQ2ODIxNTI_zh_4.mp4
    '''
