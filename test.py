# -*- coding: utf-8 -*-
import turtle
import time


ksFont = {
    'aedf':0,
    'bdcd':1,
    'ccda':2,
    'aced':3,
    'abcf':4,
    'bdaa':5,
    'afce':6,
    'cfbe':7,
    'aedd':8,
    'bfad':9,
}

ksText = "붪쳚쾾.뾭w"
for k in ksText:
    kf = k.encode('unicode_escape').decode('utf-8')[2:]
    print(ksFont[str(kf)])