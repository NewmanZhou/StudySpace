# -*- coding: utf-8 -*-
# @Time   : 2021/1/18 11:21 上午
# @Author : NewmanZhou
# @Desc : ==============================================
# Life is Short I Use Python!!!                      ===
# If this runs wrong,don't ask me,I don't know why;  ===
# If this runs right,thank god,and I don't know why. ===
# Maybe the answer,my friend,is blowing in the wind. ===
# ======================================================
# @Project : StudySpace
# @FileName: captcha_util.py.py
# @Software: PyCharm
import base64
import json

import requests
import aiofiles
from common.build_conn import BuildConn
from common.constants import constants
from utils.config_util import ConfigUtil
from utils.fateadom import FateadmApi
from utils.threadlocal import TheadLocal


class CaptchaUtil(object):

    def __init__(self, *args, **kwargs):
        self.logger = TheadLocal.getThreadLocalLogger()
        self.env = TheadLocal.getEnv()
        self.build_conn = BuildConn()
        self.config = ConfigUtil(constants[self.env].CONFIG_PATH)

    async def get_captcha_from_jjsj(self, picture_path):
        '''
        从尖叫数据识别图片验证码
        :param picture_path: 验证码路径
        :return:
        '''
        appCode = self.config.get('jjsj', 'appCode')
        appKey = self.config.get('jjsj', 'appKey')
        appSecret = self.config.get('jjsj', 'appSecret')
        base_url = 'http://apigateway.jianjiaoshuju.com'
        headers = {
            'appCode': appCode,
            'appKey': appKey,
            'appSecret': appSecret
        }
        try:
            async with aiofiles.open(picture_path, 'rb') as f:
                binary_data = await f.read()
        except IOError as e:
            self.logger.error(f'{picture_path}: {e.__class__.__name__} {e}')
            return None
        url = f'{base_url}/api/v_1/yzm.html'
        base64_data = base64.b64encode(binary_data)
        v_pic = 'data:image/jpeg;base64,{}'.format(base64_data.decode())
        data = {'v_pic': v_pic, 'v_type': 'ne4'}
        res = await self.build_conn.request(url, data=data, headers=headers)
        return res.get('v_code') or None

    async def get_captcha_from_baidu(self, picture_path):
        apiKey = self.config.get('baidu', 'APIKey')
        secretKey = self.config.get('baidu', 'SecretKey')
        host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&' \
               'client_id={}&client_secret={}'.format(apiKey, secretKey)
        response = requests.get(host)
        if response:
            print(response.json().get("access_token"))
        return response.json().get("access_token")

    def get_captcha_from_feifei(self, picture_path, pred_type="30400"):
        '''
        斐斐打码--网络图片文字识别
        '''
        pd_id = self.config.get('feifei', 'pdId')
        pd_key = self.config.get('feifei', 'pdKey')
        app_id = self.config.get('feifei', 'appId')
        app_key = self.config.get('feifei', 'appKey')
        api = FateadmApi(app_id, app_key, pd_id, pd_key)
        rsp = api.PredictFromFile(pred_type, picture_path)  # 返回识别结果的详细信息
        return json.loads(rsp.get("RspData"))['result']


