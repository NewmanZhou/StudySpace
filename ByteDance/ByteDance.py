# -*- coding: utf-8 -*-
# @Time   : 2019/10/10 上午9:38
# @Author : NewmanZhou
# @Desc : ==============================================
# Life is Short I Use Python!!!                      ===
# If this runs wrong,don't ask me,I don't know why;  ===
# If this runs right,thank god,and I don't know why. ===
# Maybe the answer,my friend,is blowing in the wind. ===
# ======================================================
# @Project : StudySpace
# @FileName: ByteDance.py
# @Software: PyCharm

# 字节跳动算法题

'''
1.得到的最少硬币数
货币系统包括1、4、16、64元共计4种硬币，以及面值为1024的纸币。
现在使用1024的纸币购买一件价值为N(0<N<=1024)的商品，问最少收到多少硬币。
'''
import math
def minnum(N):
    num = 0
    res = 1024 - N
    for i in [64, 16, 4, 1]:
        # 向下取整数。 向上取整数用 math.ceil
        num += math.floor(res / i)
        res = res % i
    return num


if __name__ == '__main__':
    print(minnum(200))
'''https://aweme.snssdk.com/aweme/v1/general/search/single/?openudid=aa864676b309bf74&version_name=8.2.0&ts=1570676268&device_type=R8207&ssmix=a&iid=88655915932&app_type=normal&os_api=19&device_id=7898061635&resolution=720*1280&device_brand=OPPO&aid=1128&manifest_version_code=820&app_name=aweme&_rticket=1570676308430&os_version=4.4.4&device_platform=android&version_code=820&update_version_code=8202&ac=wifi&dpi=320&uuid=865685026456493&language=zh&channel=douyin_tengxun_wzl'''
'''https://aweme.snssdk.com/aweme/v1/general/search/single/?keyword=966323936&offset=0&count=10&is_pull_refresh=0&hot_search=0&latitude=0.0&longitude=0.0&ts=1570677421&js_sdk_version=1.2.2&app_type=normal&manifest_version_code=310&_rticket=1570677421223&ac=wifi&device_id=53910643127&iid=48828704455&os_version=9&channel=douyin_tengxun_wzl&version_code=310&device_type=ONEPLUS%2520A6000&language=zh&uuid=869897033037051&resolution=1080%2A2200&openudid=0061ee21378e2667&update_version_code=3102&app_name=aweme&version_name=3.1.0&os_api=28&device_brand=OnePlus&ssmix=a&device_platform=android&dpi=420&aid=1128&as=a1655c4d14bffb4edb6899&cp=c4f2ba5f44b8d2e4e1aiOm&mas=01ba655c793ea7e1590398abacaa88d2d99c9c1c6c4626a62c4666'''