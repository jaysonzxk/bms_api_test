"""
author： mask
filename: get_user_bet_details.py
datetime： 2021/4/6 11:22 
ide： PyCharm
"""
from common.base import get_response, get_host, get_phone
from test_data.read_data import get_test_data
from common.logger import Log
from interfaces.user_info import getUserInfo
from common.bms_login import getBmsToken
from common.tojsonstr import getJsonStr
import json


class userBetDetails:
    """
    会员中心--回去会员注单详情
    """

    def __init__(self):
        self.log = Log()
        self.test_data = get_test_data('bms_test_data.xlsx', 'memberCentre', 7)
        self.user_id = getUserInfo().get_user_info()['data']['userId']
        self.url = get_host('test') + self.test_data['url']
        self.data = self.test_data['data']
        self.header = json.loads(self.test_data['header'])
        self.header['authorization'] = getBmsToken().get_token()
        self.method = self.test_data['method']

    def get_user_bet_details(self):
        """
        bms后台获取会员注单详情
        :return:
        """
        try:
            resp = get_response(self.url, self.method, data=self.data, headers=self.header)  # 未解密接口返回
            resp_str = getJsonStr(resp.json()['data']).get_json_str()  # 解密接口返回数据
            resp = resp.json()
            resp['data'] = resp_str['data']
            return resp
        except Exception as e:
            self.log.error('bms后台获取会员注单详情接口异常:{}，请检查'.format(str(e)))
