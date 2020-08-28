# -*- coding: utf-8 -*-
# @Time   : 2020/8/27 2:15 下午
# @Author : NewmanZhou
# @Desc : ==============================================
# Life is Short I Use Python!!!                      ===
# If this runs wrong,don't ask me,I don't know why;  ===
# If this runs right,thank god,and I don't know why. ===
# Maybe the answer,my friend,is blowing in the wind. ===
# ======================================================
# @Project : StudySpace
# @FileName: FlaskServer.py
# @Software: PyCharm
from flask import Flask,request
import json
from pymongo import MongoClient
import pymongo

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/douyin',methods=['POST'])
def abstract_content():
    data = request.get_data()
    item = json.loads(data)
    print(item)
    try:
        mgdb["douyin"].save(item)
    except pymongo.errors.DuplicateKeyError as e:
        mgdb["douyin"].update_one({'uri':item['uri']},{'$set': {'sourceUrl':item['sourceUrl']}})
        print("更新成功")
        print("MongodbSave Errot: " + str(e))
    return "请求成功"


if __name__ == '__main__':
    uri = 'mongodb://%s:%s/%s' % ('127.0.0.1', 27017, 'admin')
    mgdb = MongoClient(uri, connect=False, maxPoolSize=5000).get_database('people_crawler')
    app.run(host='0.0.0.0', port=8080)