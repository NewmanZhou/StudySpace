# -*- coding: utf-8 -*-
# @Time   : 2020/1/13 10:51 上午
# @Author : NewmanZhou
# @Desc : ==============================================
# Life is Short I Use Python!!!                      ===
# If this runs wrong,don't ask me,I don't know why;  ===
# If this runs right,thank god,and I don't know why. ===
# Maybe the answer,my friend,is blowing in the wind. ===
# ======================================================
# @Project : StudySpace
# @FileName: login_qzone.py
# @Software: PyCharm

'''
登陆QQ空间，获取登陆后cooikes中的 skey
'''
import time, re, json, requests
from selenium import webdriver


def start_chrome():
    chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument('--headless')
    # chrome_options.add_argument('--disable-gpu')
    # chrome_options.add_argument('--no-sandbox')
    # driver = webdriver.Chrome(chrome_options=chrome_options)
    SPLASH_URL = "http://39.105.14.86:8050/"
    driver = webdriver.Chrome()
    driver.get("https://mail.qq.com/")
    time.sleep(3)
    driver.switch_to.frame("login_frame")
    # driver.find_element_by_xpath('//a[@id="switcher_plogin"]').click()
    driver.find_element_by_xpath('//input[@id="u"]').send_keys("737380655")
    driver.find_element_by_xpath('//input[@id="p"]').send_keys("paeryizha1992")
    driver.find_element_by_xpath('//input[@id="login_button"]').click()
    time.sleep(2)
    qm_ptsk = driver.get_cookie("qm_ptsk")
    print(qm_ptsk.get("value").split("&"))
    print("\n")

    time.sleep(10)
    driver.quit()


def get_text_by_splash_lua():
    splash_url = "http://39.105.14.86:8050/"
    lua_script = "function main(splash)" \
                 "  splash:go('https://mail.qq.com')" \
                 "  splash:wait(0.5)" \
                 "  return {" \
                 "      html = splash:html()," \
                 "      png = splash:png()," \
                 "      har = splash:har()," \
                 "  }" \
                 "end"


    USER_AGENTS = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
    url = "https://mail.qq.com"
    url_u = splash_url + lua_script + "&url={}".format(url) #+ "&ua={}".format(USER_AGENTS)
    response = requests.get(url_u)
    print(response.content)

if __name__ == '__main__':
    start_chrome()
    # get_text_by_splash_lua()