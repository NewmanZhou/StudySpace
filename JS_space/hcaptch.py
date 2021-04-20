# -*- coding: utf-8 -*-
# @Time   : 2021/3/26 7:59 下午
# @Author : NewmanZhou
# @Desc : ==============================================
# Life is Short I Use Python!!!                      ===
# If this runs wrong,don't ask me,I don't know why;  ===
# If this runs right,thank god,and I don't know why. ===
# Maybe the answer,my friend,is blowing in the wind. ===
# ======================================================
# @Project : StudySpace
# @FileName: hcaptch.py
# @Software: PyCharm


# https://github.com/2captcha/2captcha-python
# 个人购买的验证码账号

import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

# pip3 install 2captcha-python
from twocaptcha import TwoCaptcha

api_key = os.getenv('APIKEY_2CAPTCHA', '6556d9bc3c8dc852af52a492e365bad8')

solver = TwoCaptcha(api_key)

try:
    result = solver.hcaptcha(
        sitekey='45fbc4de-366c-40ef-9274-9f3feca1cd6c',
        url='https://spyhackerz.org/',
    )

except Exception as e:
    sys.exit(e)

else:
    sys.exit('solved: ' + str(result))