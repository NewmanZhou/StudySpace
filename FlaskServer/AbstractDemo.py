# -*- coding: utf-8 -*-
# @Time   : 2020/8/7 10:56 上午
# @Author : NewmanZhou
# @Desc : ==============================================
# Life is Short I Use Python!!!                      ===
# If this runs wrong,don't ask me,I don't know why;  ===
# If this runs right,thank god,and I don't know why. ===
# Maybe the answer,my friend,is blowing in the wind. ===
# ======================================================
# @Project : StudySpace
# @FileName: AbstractDemo.py
# @Software: PyCharm
from gne import GeneralNewsExtractor
import requests

myHeader = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:55.0) Gecko/20100101 Firefox/55.0',
        }
r = requests.get( "https://www.zhihu.com/question/292189961/answer/1144339393", headers=myHeader)
extractor = GeneralNewsExtractor()
result = extractor.extract(r.text)
print(result)