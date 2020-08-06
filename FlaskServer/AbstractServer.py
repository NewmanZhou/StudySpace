# -*- coding: utf-8 -*-
# @Time   : 2020/8/6 9:05 下午
# @Author : NewmanZhou
# @Desc : ==============================================
# Life is Short I Use Python!!!                      ===
# If this runs wrong,don't ask me,I don't know why;  ===
# If this runs right,thank god,and I don't know why. ===
# Maybe the answer,my friend,is blowing in the wind. ===
# ======================================================
# @Project : StudySpace
# @FileName: AbstractServer.py
# @Software: PyCharm
from flask import Flask,request
import json

from FlaskServer.GetTitleAndContent import GetTitleAndContent

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/abstract',methods=['POST'])
def abstract_content():
    data = request.get_data()
    json_data = json.loads(data)
    url = json_data.get('url')
    return abstrct.getTitleAndContent(url)


if __name__ == '__main__':
    abstrct = GetTitleAndContent()
    app.run(host='0.0.0.0', port=8080)