# -*- coding: utf-8 -*-
# @Time   : 2021/1/15 11:24 上午
# @Author : NewmanZhou
# @Desc : ==============================================
# Life is Short I Use Python!!!                      ===
# If this runs wrong,don't ask me,I don't know why;  ===
# If this runs right,thank god,and I don't know why. ===
# Maybe the answer,my friend,is blowing in the wind. ===
# ======================================================
# @Project : StudySpace
# @FileName: SeleniumTor.py
# @Software: PyCharm
import os
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium import webdriver


# path to the firefox binary inside the Tor package
binary = '/Applications/Tor Browser.app/Contents/MacOS/firefox'
if os.path.exists(binary) is False:
    raise ValueError("The binary path to Tor firefox does not exist.")
firefox_binary = FirefoxBinary(binary)


browser = None
def get_browser(binary=None):
    global browser
    # only one instance of a browser opens, remove global for multiple instances
    if not browser:
        browser = webdriver.Firefox(firefox_binary=binary,timeout=120)
    return browser

if __name__ == "__main__":
    browser = get_browser(binary=firefox_binary)
    urls = (
        ('tor browser check', 'https://check.torproject.org/'),
        ('ip checker', 'http://icanhazip.com')
    )
    for url_name, url in urls:
        print("getting", url_name, "at", url)
        browser.get(url)