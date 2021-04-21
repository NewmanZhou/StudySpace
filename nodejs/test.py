# -*- coding: utf-8 -*-
# @Time   : 2021/4/20 10:12 上午
# @Author : NewmanZhou
# @Desc : ==============================================
# Life is Short I Use Python!!!                      ===
# If this runs wrong,don't ask me,I don't know why;  ===
# If this runs right,thank god,and I don't know why. ===
# Maybe the answer,my friend,is blowing in the wind. ===
# ======================================================
# @Project : StudySpace
# @FileName: test.py.py
# @Software: PyCharm

import requests

if __name__ == '__main__':
    url = "http://localhost:3000/get_num"
    data = {"a": 1, "b": 5}
    req = requests.post(url,data)
    print(req.text)
