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
from mitmproxy import ctx

def request(flow):
    pass

def response(flow):
    # 忽略相应的地址
    # host = flow.request.host

    url = flow.request.url
    postUrl = "http://0.0.0.0:8080/douyin"

    '''
    /aweme/v1/aweme/post/?source=0&user_avatar_shrink=96_96&
    video_cover_shrink=248_330&publish_video_strategy_type=2
    &max_cursor=0&sec_user_id=MS4wLjABAAAAaHR-JiNflRpCBmfchuxJRL_fdexZHbzB2ldb46rYIhk&
    count=20&is_order_flow=0&_rticket=1606376601119&
    cpu_support64=true&host_abi=armeabi-v7a&appTheme=dark&ts=1606376612&
    '''
    if "video_cover_shrink" in url:
        ctx.log.warn(url)
        aweme_list = json.loads(flow.response.content)['aweme_list']
        requests.post(postUrl, json.dumps(aweme_list))
        for obj in aweme_list:
            ctx.log.error(str(obj))
            # print(str(obj))
            item = dict()
            item['uri'] = obj['video']['play_addr']['uri']
            item['author'] = obj['author']['nickname']
            item['author_user_id'] = obj['author_user_id']
            # item['share_qrcode_uri'] = share_qrcode_uri
            sourceUrl = obj['video']['play_addr']['url_list'][0]
            # item['sourceUrl'] = re.search("(.*?)\?", sourceUrl).group(1)
            item['sourceUrl'] = sourceUrl[0]
            item['title'] = obj['desc']
            item['type'] = 0

            res = requests.post(postUrl, json.dumps(item))
            ctx.log.warn(res.status_codeq)
            ctx.log.warn(item)


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


