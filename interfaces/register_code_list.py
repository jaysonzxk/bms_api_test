"""
author： mask
filename: register_code_list.py
datetime： 2021/4/6 16:04 
ide： PyCharm
"""
from common.base import get_response, get_host
from test_data.read_data import get_test_data
from common.logger import Log
from interfaces.user_info import getUserInfo
from common.bms_login import getBmsToken
from common.tojsonstr import getJsonStr
import json


class registerCodeList:
    """
    会员中心--注册码管理列表
    """

    def __init__(self):
        self.log = Log()
        self.test_data = get_test_data('bms_test_data.xlsx', 'memberCentre', 18)
        self.url = get_host('test') + self.test_data['url']
        self.data = self.test_data['data']
        self.header = json.loads(self.test_data['header'])
        self.header['authorization'] = getBmsToken().get_token()
        self.method = self.test_data['method']

    def register_code_list(self):
        """
        注册码管理列表
        :return:
        """
        try:
            resp = get_response(self.url, self.method, data=self.data, headers=self.header)  # 未解密接口返回
            resp_str = getJsonStr(resp.json()['data']).get_json_str()  # 解密接口返回数据
            resp = resp.json()
            resp['data'] = resp_str['data']
            return resp
        except Exception as e:
            self.log.error('bms后台获取注册码列表接口异常:{}，请检查'.format(str(e)))


# if __name__ == '__main__':
#     res = registerCodeList().register_code_list()
#     print(res)