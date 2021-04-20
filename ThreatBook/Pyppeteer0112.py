import asyncio, json, re, time
from pyppeteer import launch
from FateadmApiClass import FateadmApi

userName = "611098"
passWord = "qwerty123"


class ChinaBlogLogin():
    async def start(self):
        js1 = '''() =>{

            Object.defineProperties(navigator,{
            webdriver:{
                get: () => false
                }
            })
        }'''
        try:
            # '--headless',
            browser = await launch(
                {'headless': False, 'args': ['--disable-automation', '--disable-gpu', '--no-sandbox',
                                             '--proxy-server=socks5://127.0.0.1:9050'], })

            page = await browser.newPage()
            await page.goto('http://xxxxxxxx3a3kuuhhw5w7stk25fzhttrlpiomij5bogkg7yyqsng5tqyd.onion',
                            {'timeout': 50 * 1000})
            await page.evaluate(js1)

            yazhengma = await page.waitFor('//fieldset[@class="fieldset_login"]//img')  # 通过css selector定位验证码元素
            await yazhengma.screenshot({'path': 'yazhengma.png'})  #
            res = self.TestFunc()
            print("验证码：%s" % res)
            await page.type('input[name=lgid]', userName, {'delay': 100})
            await page.type('input[name=lgpass]', passWord, {'delay': 100})
            await page.type('input[name=sub_code]', res, {'delay': 100})
            ele = await page.waitForXPath('//input[@class="login_botton"]')
            await ele.click()  # 点击页面元素
            print("登录点击")
            await page.waitFor(1000 * 8)
            print("等待结束")
            '''
            登录成功的Url
            'http://xxxxxxxx3a3kuuhhw5w7stk25fzhttrlpiomij5bogkg7yyqsng5tqyd.onion/index.php'
            '''
            # 获取登录成功的页面属性 进行判断是否成功登录。

            # divuserbar = await page.waitFor('//div[@class="div04"]')
            # print(divuserbar)
            if "/login.php" not in page.url:
                cookie = await page.cookies()
                return cookie
            else:
                print("登录失败了")
                page.content()
                await page.close()
                # asyncio.get_event_loop().run_until_complete(self.start())
        except Exception as e:
            print("ERROR: %s" % e)
            # await asyncio.get_event_loop().run_until_complete(self.start())

    def TestFunc(self):
        # pd账号秘钥，请在用户中心页获取
        pd_id = "127292"
        pd_key = "D+Wf6PwODfCUcjHf/hEDJetHae2QNxiX"
        app_id = "327292"
        app_key = "bsKzFtEaf7/5jZfI0aO5tTjf50gLY+/K"
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
    chinaBlog = ChinaBlogLogin()
    cookies = asyncio.get_event_loop().run_until_complete(chinaBlog.start())
    print(cookies)
