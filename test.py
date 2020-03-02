# -*- coding: utf-8 -*-
import turtle
import time,datetime


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

# ksText = "붪쳚쾾.뾭w"
# for k in ksText:
#     kf = k.encode('unicode_escape').decode('utf-8')[2:]
#     print(ksFont[str(kf)])


def timestamp_to_otherStyleTime(timestamp, return_datetime=False):
    """时间戳转字符串或者datetime.datetime类型"""
    if not timestamp:
        return
    tp = int(timestamp) if len(str(timestamp)) < 13 else int(timestamp) // 1000

    if return_datetime:
        return datetime.fromtimestamp(tp)
    else:
        timearray = time.localtime(tp)
        return time.strftime("%Y-%m-%d %H:%M:%S", timearray)

timestamp = "1583039959850"
print(timestamp_to_otherStyleTime(timestamp))