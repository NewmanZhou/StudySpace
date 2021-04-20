# -*- coding: utf-8 -*-
# @Time   : 2021/2/5 11:06 上午
# @Author : NewmanZhou
# @Desc : ==============================================
# Life is Short I Use Python!!!                      ===
# If this runs wrong,don't ask me,I don't know why;  ===
# If this runs right,thank god,and I don't know why. ===
# Maybe the answer,my friend,is blowing in the wind. ===
# ======================================================
# @Project : StudySpace
# @FileName: selenium_goolge.py
# @Software: PyCharm
# 参考地址：
# https://blog.csdn.net/u014524046/article/details/106924120

from selenium import webdriver

print('开始...')
options = webdriver.ChromeOptions()
# options.add_argument('--headless')
options.add_argument('--no-sandbox')

driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get('https://www.baidu.com/')
print(driver.title)
driver.quit()
print('结束！')
