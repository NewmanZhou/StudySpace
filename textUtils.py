# -*- coding=utf-8-*-
import base64 ,time ,hashlib , requests
from pyDes import des, PAD_PKCS5, CBC

def getMD5():
    s = 'equtype=ANDROID&loginImei=Android358240051111110&timeStamp=1597829003892&userPwd=qwerty&username=16688889999&key=sdlkjsdljf0j2fsjk'
    # s.encode()#变成bytes类型才能加密
    m = hashlib.md5(s.encode())
    print(m.hexdigest().upper())

def getReqBody():
    KEY = base64.urlsafe_b64decode("w9JtyoYll4I=")
    IV = base64.urlsafe_b64decode("MzIwMjgwOTI=")
    data = '{"equtype":"ANDROID","loginImei":"Android358240051111110","sign":"AA6D08F069DB7C8BD04779FCCF3B8CDD","timeStamp":"1597829699467","userPwd":"qwerty","username":"18519728110"}'.encode("utf-8")
    des_obj = des(KEY, CBC, IV, padmode=PAD_PKCS5)  # 初始化一个des对象，参数是秘钥，加密方式，偏移， 填充方式

    secret_bytes = des_obj.encrypt(data)
    return (base64.standard_b64encode(secret_bytes))


def login():
    headers = {
        'If-Modified-Since': 'Tue, 18 Aug 2020 09:18:09 GMT+00:00',
        'Content-Type': 'application/json; charset=utf-8',
        'User-Agent': 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; Android SDK built for x86 Build/KK)',
        'Host': 'api.dodovip.com',
    }

    data = '{"Encrypt":"NIszaqFPos1vd0pFqKlB42Np5itPxaNH//FDsRnlBfgL4lcVxjXii4oHXYj/wLHH40VHAnW5AWkUjKsU3M6MCVuWQa5JsW3nhEAzXnjVBtTRWQm9BELZ+ESZw5LYufDrxVBW4u5Jx3W2tdA57m90Qx8ZvIoyhAn2F1Pr9TwA7jta8aR56s/X4Ej7ab6OknCeRTD59OPSGSzBT1pDGSHdPgVFo8OZxpZxGZ+7vfklJc="}'

    response = requests.post('http://api.dodovip.com/api/user/login', headers=headers, data=data)
    print(response.status_code)
    print(response.text)

if __name__ == '__main__':
    print(getReqBody())
    # getReqBody()

'''
https://c-ssl.duitang.com/uploads/item/201912/09/20191209190342_lkojb.thumb.700_0.jpg
https://c-ssl.duitang.com/uploads/item/201912/09/20191209190342_lkojb.jpg"

https://c-ssl.duitang.com/uploads/item/201912/09/20191209191321_olbex.thumb.700_0.jpg
https://c-ssl.duitang.com/uploads/people/202008/22/20200822203333_MkzWi.thumb.700_0.jpg

https://221.228.82.177/napi/blog/list/by_filter_id/?filter_id=%E7%88%B1%E8%B1%86-%E6%9E%97%E5%BD%A6%E4%BF%8A-%E5%A3%81%E7%BA%B8heap&include_fields=sender%2Calbum%2Cicon_url%2Clike_count%2Creply_count&start=0&screen_width=1080&locale=zh&app_version=7.9.7.2&platform_name=Android&app_code=nayutas&screen_height=1920&platform_version=5.1&__domain=www.duitang.com
https://221.228.82.177/napi/blog/detail/?include_fields=share_links_3,tags,related_albums,related_albums.covers,top_like_users,extra_html&blog_id=1162680424&__domain=www.duitang.com

'''