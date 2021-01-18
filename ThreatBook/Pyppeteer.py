# -*- coding: utf-8 -*-
# @Time   : 2021/1/17 1:55 下午
# @Author : NewmanZhou
# @Desc : ==============================================
# Life is Short I Use Python!!!                      ===
# If this runs wrong,don't ask me,I don't know why;  ===
# If this runs right,thank god,and I don't know why. ===
# Maybe the answer,my friend,is blowing in the wind. ===
# ======================================================
# @Project : StudySpace
# @FileName: Pyppeteer.py
# @Software: PyCharm
import asyncio
import json
from pyppeteer import launch
from FateadmApiClass import FateadmApi

userName = "611098"
passWord = "qwerty123"


async def main():
    '''
    chromium浏览器多开页面卡死问题
    解决这个问题的方法就是浏览器初始化的时候添加’dumpio’:True。至于什么原理我也不知道，只是添加上了。

    浏览器窗口很大，内容显示很小
    上面的问题是需要设置浏览器显示大小，默认就是无法正常显示。
    '''
    # browser = await launch(
    #     {'headless': False, 'dumpio': True, 'autoClose': False, 'args': ['--no-sandbox', '--window-size=1366,850']})
    # await page.setViewport({'width': 1366, 'height': 768})

    browser = launch(headless=False, args=['--disable-infobars', '--proxy-server=socks5://127.0.0.1:9050'])
    page = await browser.newPage()
    await page.evaluate(
        '''() =>{ Object.defineProperties(navigator,{ webdriver:{ get: () => false } }) }''')
    await page.goto('http://xxxxxxxx3a3kuuhhw5w7stk25fzhttrlpiomij5bogkg7yyqsng5tqyd.onion', {'timeout': 100 * 1000})
    page.waitForNavigation(),
    await page.screenshot(path="test_screenshot.png")
    yazhengma = await page.waitFor('//fieldset[@class="fieldset_login"]//img')  # 通过css selector定位验证码元素
    await yazhengma.screenshot({'path': 'yazhengma.png'})  #
    res = TestFunc()
    print(res)
    await page.type('input[name=lgid]', userName, {'delay': 100})
    await page.type('input[name=lgpass]', passWord, {'delay': 100})
    # await page.type('input[name=sub_code]', res, {'delay': 100})
    ele = await page.waitForXPath('//input[@class="login_botton"]')
    print(ele)
    await ele.click()  # 点击页面元素
    cookie = await page.cookies()
    print(cookie)

    await asyncio.sleep(100)


def TestFunc():
    # pd账号秘钥，请在用户中心页获取
    pd_id = "127269"
    pd_key = "vhWINpOkqYgrwHttFUZ7Xyc584iRicnO"
    app_id = "327269"
    app_key = "M0nidCmn1yG4mB1uOR8wbH0oEdrVCCju"
    # 具体类型可以查看官方网站的价格页选择具体的类型，不清楚类型的，可以咨询客服
    pred_type = "20400"
    # 初始化api接口
    api = FateadmApi(app_id, app_key, pd_id, pd_key)
    # 查询余额接口
    # balance = api.QueryBalcExtend()  # 直接返余额
    # api.QueryBalc()

    # 通过文件识别验证码
    # 通过文件进行验证码识别,请使用自己的图片文件替换
    # 如果是通过url直接获取内存图片，这直接调用 Predict接口就好
    file_name = "yazhengma.png"
    # res =  api.PredictFromFileExtend(pred_type,file_name)  	# 直接返回识别结果
    # 多网站类型时，需要增加src_url参数，具体请参考api文档: http://docs.fateadm.com/web/#/1?page_id=6
    rsp = api.PredictFromFile(pred_type, file_name)  # 返回识别结果的详细信息
    result = json.loads(rsp.get("RspData"))['result']
    return result


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
