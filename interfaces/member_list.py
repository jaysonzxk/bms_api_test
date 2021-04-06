"""
author： mask
filename: member_list.py
datetime： 2021/4/5 13:36 
ide： PyCharm
"""
from common.base import get_response, get_host
from test_data.read_data import get_test_data
from common.logger import Log
from common.bms_login import getBmsToken
from common.tojsonstr import getJsonStr
import json


class memberList:
    """
    会员中心-获取会员列表
    """

    def __init__(self):
        self.log = Log()
        self.test_data = get_test_data('bms_test_data.xlsx', 'memberCentre', 0)
        self.url = get_host('test') + self.test_data['url']
        self.data = json.loads(self.test_data['data'])
        self.header = json.loads(self.test_data['header'])
        self.header['authorization'] = getBmsToken().get_token()
        self.method = self.test_data['method']

    def get_member_isOperate_list(self):
        """
        bms-获取所有正式账号列表
        :return:
        """
        try:
            resp = get_response(self.url, self.method, data=json.dumps(self.data), headers=self.header)  # 未解密接口返回
            resp_str = getJsonStr(resp.json()['data']).get_json_str()  # 解密接口返回数据
            resp = resp.json()
            resp['data'] = resp_str['data']
            return resp
        except Exception as e:
            self.log.error('bms后台获取所有会员列表接口异常:{}，请检查'.format(str(e)))

    def get_member_noOperate_list(self):
        """
        bms-获取所有运营账号列表
        :return:
        """
        self.data['searchParam']['isOperate'] = "true"
        try:
            resp = get_response(self.url, self.method, data=json.dumps(self.data), headers=self.header)  # 未解密接口返回
            resp_str = getJsonStr(resp.json()['data']).get_json_str()  # 解密接口返回数据
            resp = resp.json()
            resp['data'] = resp_str['data']
            return resp
        except Exception as e:
            self.log.error('bms后台获取所有会员列表接口异常:{}，请检查'.format(str(e)))


