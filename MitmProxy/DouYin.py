# -*- coding: utf-8 -*-
# @Time   : 2020/8/26 3:00 下午
# @Author : NewmanZhou
# @Desc : ==============================================
# Life is Short I Use Python!!!                      ===
# If this runs wrong,don't ask me,I don't know why;  ===
# If this runs right,thank god,and I don't know why. ===
# Maybe the answer,my friend,is blowing in the wind. ===
# ======================================================
# @Project : StudySpace
# @FileName: DouYin.py
# @Software: PyCharm
import json, requests, os, re


def response(flow):
    # 忽略相应的地址
    host = flow.request.host
    url_filter = ['www.baidu.com', 'm.baidu.com', 'mbd.baidu.com', 'www.google.com', 'www.qq.com', 'www.youku.com',
                  'h5.dingtalk.com']
    url_douyin = ['aweme.snssdk.com']

    # if host in url_filter:
    #     return
    #
    # if not flow.request.method == "GET":
    #     return
    #
    # if not flow.response.status_code == 200:
    #     return

    url = flow.request.url
    postUrl = "http://0.0.0.0:8080/douyin"
    # if host in url_douyin and "sec_user_id" in url:
    # if host in url_douyin and "sec_user_id" in url:
    if "sec_user_id" in url:
        print(url)
        aweme_list = json.loads(flow.response.content)['aweme_list']
        # author = re.search('"author":(\d+)', flow.response.content).group(1)
        # author_user_id = re.search('"author_user_id":(\d+)', flow.response.content).group(1)
        # share_qrcode_uri =  re.search('"share_qrcode_uri":(\d+)', flow.response.content).group(1)
        for obj in aweme_list:
            item = dict()
            item['uri'] = obj['video']['play_addr']['uri']
            item['author'] = obj['author']['nickname']
            item['author_user_id'] = obj['author_user_id']
            # item['share_qrcode_uri'] = share_qrcode_uri
            sourceUrl = obj['video']['play_addr']['url_list'][0]
            item['sourceUrl'] = re.search("(.*?)\?", sourceUrl).group(1)
            item['title'] = obj['desc']
            item['type'] = 0
            requests.post(postUrl, json.dumps(item))
            print(item)


def download(video_obj):
    try:
        download_dir = "/Users/newmanzhou/Downloads/douyin/"
        file_name = '%s%s.mp4' % (download_dir, video_obj['title'])
        # print("Downloading file:%s" % file_name)
        r = requests.get(video_obj['sourceUrl'], stream=True)
        with open(file_name, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024 * 1024):
                if chunk:
                    f.write(chunk)
                    print("%s downloaded!\n" % file_name)
    except Exception as e:
        print(e)
        download(video_obj)


def getFileName(file_dir):
    FileList = []
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            if os.path.splitext(file)[1] == '.mp4':
                FileList.append(file)
    return FileList


# def saveMoogodb(item):
#     mgdb = MongodbClient()
#     mgdb['douyin'].save(item)


'''
https://aweme.snssdk.com/aweme/v1/aweme/post/?source=0&max_cursor=0&sec_user_id=MS4wLjABAAAA3c7xW7c5S4hBOxr-zIovs2Tvf2dLmHGJRfzl4Il2t9HypB5oevPddH6kZaakrMJt&count=20&os_api=22&device_type=PRO%205&ssmix=a&manifest_version_code=110200&dpi=480&uuid=867905028376327&app_name=douyin_lite&version_name=11.2.0&ts=1598429291&app_type=normal&ac=wifi&update_version_code=11209900&channel=meizu&_rticket=1598429296204&device_platform=android&iid=2145853173144999&version_code=110200&mac_address=68%3A3E%3A34%3A9D%3A0C%3ACB&cdid=c61177f2-faad-4342-b09d-ee8cc7edda18&openudid=b89b6e7796b5d448&device_id=49225975640&resolution=1080*1920&os_version=5.1&language=zh&device_brand=Meizu&aid=2329
'''
