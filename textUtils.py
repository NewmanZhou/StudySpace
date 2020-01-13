# -*- coding: utf-8 -*-
# @Time   : 2019/12/31 3:20 下午
# @Author : NewmanZhou
# @Desc : ==============================================
# Life is Short I Use Python!!!                      ===
# If this runs wrong,don't ask me,I don't know why;  ===
# If this runs right,thank god,and I don't know why. ===
# Maybe the answer,my friend,is blowing in the wind. ===
# ======================================================
# @Project : StudySpace
# @FileName: textUtils.py
# @Software: PyCharm


import redis


def redis_clent():
    # host = '127.0.0.1'
    host = 'r-2zeelgy4aqm46uzipi.redis.rds.aliyuncs.com'
    port = 6379
    db = 2
    password = 'h6GD4#b9IvRB8A%e'
    pool = redis.ConnectionPool(host=host, port=port, password=password, db=db, decode_responses=True)
    redis_db = redis.Redis(connection_pool=pool)

    return redis_db


if __name__ == '__main__':
    k = 0
    while True:
        if k < 10:
            k += 1
            print(k)
        else:
            break

    redis_db = redis_clent()
    print(redis_db.llen("low"))
