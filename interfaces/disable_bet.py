"""
author： mask
filename: disable_bet.py
datetime： 2021/4/6 14:46 
ide： PyCharm
"""
from common.base import get_response, get_host
from test_data.read_data import get_test_data
from common.logger import Log
from databases.database import databaseOperations
from common.bms_login import getBmsToken
from common.tojsonstr import getJsonStr
import json


class disableBet:
    """
    会员中心--禁止会员投注
    """

    def __init__(self):
        self.log = Log()
        self.test_data = get_test_data('bms_test_data.xlsx', 'memberCentre', 11)
        self.url = get_host('test') + self.test_data['url']
        self.header = json.loads(self.test_data['header'])
        self.header['authorization'] = getBmsToken().get_token()
        self.method = self.test_data['method']

    def disable_bet(self):
        """
        禁止会员投注
        :return:
        """
        try:
            resp = get_response(self.url, self.method, headers=self.header)  # 未解密接口返回
            resp_str = getJsonStr(resp.json()['data']).get_json_str()  # 解密接口返回数据
            resp = resp.json()
            resp['data'] = resp_str['data']
            return resp
        except Exception as e:
            self.log.error('bms后台禁止会员投注接口异常:{}，请检查'.format(str(e)))