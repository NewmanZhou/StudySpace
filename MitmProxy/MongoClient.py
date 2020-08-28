# -*- coding: utf-8 -*-
# @Time   : 2020/8/27 9:28 上午
# @Author : NewmanZhou
# @Desc : ==============================================
# Life is Short I Use Python!!!                      ===
# If this runs wrong,don't ask me,I don't know why;  ===
# If this runs right,thank god,and I don't know why. ===
# Maybe the answer,my friend,is blowing in the wind. ===
# ======================================================
# @Project : StudySpace
# @FileName: MongoClient.py
# @Software: PyCharm
from pymongo import MongoClient
import requests, os, time
from bson.objectid import ObjectId


class MongodbClient():
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(MongodbClient, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        uri = 'mongodb://%s:%s/%s' % ('127.0.0.1', 27017, 'admin')
        self.mgdb = MongoClient(uri, connect=False, maxPoolSize=5000).get_database('people_crawler')

    # def update(self,item):
    #     self.mgdb[''].update({'title':'MongoDB 教程'},{'$set':item})

    def getClient(self):
        return self.mgdb

    def download(self, video_obj):
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Mobile Safari/537.36',
            'Accept': '*/*',
            'Referer': 'http://v6-dy.ixigua.com/89f5f62ab66373446dc08d005e68d6f6/5f487b72/video/tos/cn/tos-cn-ve-15/b17b592290674a1cac07d45b98cf94f3/',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Range': 'bytes=0-',
        }
        download_dir = "/Users/newmanzhou/Downloads/douyin/%s/" % video_obj['author']
        download_url = "https://aweme.snssdk.com/aweme/v1/play/?video_id=%s&line=0" % video_obj['uri']
        self.mkdir(download_dir)
        file_name = '%s%s.mp4' % (download_dir, video_obj['title'])
        r = requests.get(video_obj["sourceUrl"], headers=headers, stream=True)
        with open(file_name, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024 * 1024):
                if chunk:
                    f.write(chunk)
            print("%s downloaded!\n" % file_name)

    def searchMongo(self):
        while True:
            datas = self.mgdb["douyin"].find({"type": 0}).limit(10)
            for data in datas:
                self.download(data)
                self.mgdb['douyin'].update({'_id': ObjectId(data['_id'])}, {'$set': {'type': 1}})
            time.sleep(10)

    def mkdir(self, path):
        # 去除首位空格
        path = path.strip()
        # 去除尾部 \ 符号
        path = path.rstrip("\\")
        # 判断路径是否存在
        # 存在     True
        # 不存在   False
        isExists = os.path.exists(path)
        # 判断结果
        if not isExists:
            # 如果不存在则创建目录
            # 创建目录操作函数
            os.makedirs(path)
            # print(path + ' 创建成功')
            return True
        else:
            # 如果目录存在则不创建，并提示目录已存在
            # print(path + ' 目录已存在')
            return False


if __name__ == '__main__':
    mgdb = MongodbClient()
    mgdb.searchMongo()

    '''
     https://aweme.snssdk.com/aweme/v1/play/?video_id=v0200f090000brtvthj2ap94303b9e80&line=0
    '''
