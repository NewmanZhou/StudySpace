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
    print(list)

def getSharlUrl():
    import requests

    cookies = {
        'kuaishou.live.web_ph': 'd9f4d4ec8df375c8545d3719cabfe659f891',
        'kuaishou.live.web_st': 'ChRrdWFpc2hvdS5saXZlLndlYi5zdBKgAZdaJBoCR7RHoqJD31H2OGxXxJX17pPdGJadubrebdiwaaEImwK_YUisOM9YAFEBkSwLdfytjFz8yeU-zRZM_M_3Uy3891qvSg2M7uKSBzyX3reGY_nmqs_coOKLzjdOVsl3lbBKAMQOd2OZIGYKCKjh7cz-eMUsTsXwvf7RfRnYYvS0dO3nu3YwrZVb4A4yWyAsGoqIL3Fn8fz0BATvAmAaEiWGLfbrnUkCqTgL7M-vFrp6OSIgm-44Ynwg-O-mDVkixO0pFVahtFTjMz4v62oz5ED7epsoBTAB',
        'userId': '1417278167',
        'client_key': '65890b29',
        'clientid': '3',
        'did': 'web_e20ead6360fe03a308d741b14117b0ef',
        'Hm_lpvt_86a27b7db2c5c0ae37fee4a8a35033ee': '1594949411',
        'Hm_lvt_86a27b7db2c5c0ae37fee4a8a35033ee': '1594949411',
        'kuaishou.live.bfb1s': '9b8f70844293bed778aade6e0a8f9942',
    }

    headers = {
        # 'Host': 'live.kuaishou.com',
        'Content-Type': 'application/json',
        # 'Origin': 'https://live.kuaishou.com',
        # 'Accept': '*/*',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
        # 'Referer': 'https://live.kuaishou.com/profile/renminwang',
        # 'Accept-Language': 'zh-cn',
    }

    data = '{"operationName":"SharePageQuery","variables":{"photoId":"3xkn3wq6vjw3vs2","principalId":"renminwang"},"query":"query SharePageQuery($principalId: String, $photoId: String) {\\n  feedById(principalId: $principalId, photoId: $photoId) {\\n    currentWork {\\n      playUrl\\n      __typename\\n    }\\n    __typename\\n  }\\n}\\n"}'

    response = requests.post('https://live.kuaishou.com/m_graphql', headers=headers,  data=data)
    print(response.text)

def getNextPage():
    import requests

    cookies = {
        'kuaishou.live.bfb1s': '9b8f70844293bed778aade6e0a8f9942',
        'clientid': '3',
        'did': 'web_37663519b71b295f41d501fb80888269',
        'client_key': '65890b29',
        'Hm_lvt_86a27b7db2c5c0ae37fee4a8a35033ee': '1594950030',
        'didv': '1594953285000',
        'Hm_lpvt_86a27b7db2c5c0ae37fee4a8a35033ee': '1595212857',
        'userId': '1417278167',
        'kuaishou.live.web_st': 'ChRrdWFpc2hvdS5saXZlLndlYi5zdBKgAVuJ0VxOxImnuBsAvRTb6BklOzkimGshGwj8tQ-4m4knhXu_HUjBWbBSzKZ4sWQCoRl4NTyXyT1CU2SoJQSTqiZCDPthyho1If-8xclkg0R0LR4I6f5Kphp9MR5SwfMl8t0QJk5VVn7-V9QiArWANNLW4T-1Q8_SaTjg9e50A713ANWTo750u9UctQ8JonB9AgvS_PTXu8rTqMCcDpd9ajAaEgVs1NUGNkhli9eUAvcJtCqMsiIgve_OUJxy8b0leYs4KHhzRPvXL4xvezKoFoS_RBBQPjkoBTAB',
        'kuaishou.live.web_ph': 'c00943c24050e561dd3c1d4bdcfdb8cf1ecc',
    }

    headers = {
        # 'Host': 'live.kuaishou.com',
        # 'Pragma': 'no-cache',
        # 'Cache-Control': 'no-cache',
        # 'accept': '*/*',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
        'content-type': 'application/json',
        # 'Origin': 'https://live.kuaishou.com',
        # 'Sec-Fetch-Site': 'same-origin',
        # 'Sec-Fetch-Mode': 'cors',
        # 'Sec-Fetch-Dest': 'empty',
        # 'Referer': 'https://live.kuaishou.com/profile/renminwang',
        # 'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    }

    data = '{"operationName":"publicFeedsQuery","variables":{"principalId":"renminwang","pcursor":"1.593665791911E12","count":24},"query":"query publicFeedsQuery($principalId: String, $pcursor: String, $count: Int) {\\n  publicFeeds(principalId: $principalId, pcursor: $pcursor, count: $count) {\\n    pcursor\\n    live {\\n      user {\\n        id\\n        avatar\\n        name\\n        __typename\\n      }\\n      watchingCount\\n      poster\\n      coverUrl\\n      caption\\n      id\\n      playUrls {\\n        quality\\n        url\\n        __typename\\n      }\\n      quality\\n      gameInfo {\\n        category\\n        name\\n        pubgSurvival\\n        type\\n        kingHero\\n        __typename\\n      }\\n      hasRedPack\\n      liveGuess\\n      expTag\\n      __typename\\n    }\\n    list {\\n      id\\n      thumbnailUrl\\n      poster\\n      workType\\n      type\\n      useVideoPlayer\\n      imgUrls\\n      imgSizes\\n      magicFace\\n      musicName\\n      caption\\n      location\\n      liked\\n      onlyFollowerCanComment\\n      relativeHeight\\n      timestamp\\n      width\\n      height\\n      counts {\\n        displayView\\n        displayLike\\n        displayComment\\n        __typename\\n      }\\n      user {\\n        id\\n        eid\\n        name\\n        avatar\\n        __typename\\n      }\\n      expTag\\n      __typename\\n    }\\n    __typename\\n  }\\n}\\n"}'

    response = requests.post('https://live.kuaishou.com/m_graphql', headers=headers, data=data)
    print(data)
    j_data = json.loads(response.text)
    list_data = jsonpath.jsonpath(j_data,"$..list")[0]
    for ld in list_data:
        caption = ld.get("caption")

if __name__ == '__main__':
    getNextPage()
