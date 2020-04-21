# -*- coding: utf-8 -*-
# @Time   : 2020/4/15 2:10 下午
# @Author : NewmanZhou
# @Desc : ==============================================
# Life is Short I Use Python!!!                      ===
# If this runs wrong,don't ask me,I don't know why;  ===
# If this runs right,thank god,and I don't know why. ===
# Maybe the answer,my friend,is blowing in the wind. ===
# ======================================================
# @Project : StudySpace
# @FileName: myMongoClient.py
# @Software: PyCharm
import pymongo



class MongoBaseRW(object):
    """基本读写Mongo库工作类"""
    db_config = None  # 数据库配置
    def __new__(cls, args):
        if not hasattr(cls, 'instance'):
            cls.instance = super(MongoBaseRW, cls).__new__(cls)
        return cls.instance

    def __init__(self, env='local', host='', port='', user='', password='', db='', collection=''):
        """
        可以配置环境，或输入连接参数
        1.环境
        env 为db_config中的连接配置,如果类属性read_only为True时，无视env直接使用read_only
        local:      myself
        test:       test  db
        online:     online db

        2.自定义连接参数：
        custom:     env 为 custom 使用后面的连接参数的配置
        """
        self.env = env
        # if env == 'custom':
        #     db_config = {
        #         'host'    : host,
        #         'port'    : port,
        #         'user'    : user,
        #         'password': password,
        #         'database'      : db,
        #         'collection'    : collection,
        #     }
        # else:
        #     db_config = self.db_config.config[env]
        #
        # self.client = pymongo.MongoClient(db_config['host'],
        #                                   db_config['port'],
        #                                   username=db_config.get('user'),
        #                                   password=db_config.get('password')
        #                                   )
        # self.db = self.client[db_config['database']]
        # try:
        #     if db_config.get('user') and db_config.get('password'):
        #         self.db.authenticate(db_config['user'], db_config['password'])
        # except:
        #     pass
        # self.base_name = db_config['collection']
        # self.coll = self.db[db_config['collection']]

    # def close(self):
    #     self.client.close()

    def insert(self, dic):
        # print("insert...")
        return self.coll.insert(dic)

    def find(self, dic=None):
        # print("find...")
        res = []
        if not dic:
            for i in self.coll.find():
                res.append(i)
        else:
            for i in self.coll.find(dic):
                res.append(i)
        return res

    def find_one(self, dic):
        # print("find_one...")
        return self.coll.find_one(dic)

    # def __del__(self):
    #     self.close()

if __name__ == '__main__':
    config = {
        'online': {  # 内网
            'host': 'dds-2ze73e1c922a43b41.mongodb.rds.aliyuncs.com',
            'user': 'root',
            'port': 3717,
            'password': 'TGIKX2csW5Ox7u!D',
            'database': 'zzpt_spider',  # todo
            'collection': 'zzpt'  # 新表存kfk_msg
        },
        'online_author': {  # 内网
            'host': 'dds-2ze73e1c922a43b41.mongodb.rds.aliyuncs.com',
            'user': 'root',
            'port': 3717,
            'password': 'TGIKX2csW5Ox7u!D',
            'database': 'zzpt_online',
            'collection': None
        },
    }
    dbspider = MongoBaseRW(config["online"])

    print(dbspider)

