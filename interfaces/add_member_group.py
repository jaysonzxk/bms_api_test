"""
author： mask
filename: add_member_group.py
datetime： 2021/4/10 11:39 
ide： PyCharm
"""
from common.base import get_response, get_host
from test_data.read_data import get_test_data
from common.logger import Log
from databases.database import databaseOperations
from common.bms_login import getBmsToken
from common.tojsonstr import getJsonStr
import json


class addMemberGroup:
    """
    会员中心-新增会员分组
    """

    def __init__(self):
        self.log = Log()
        self.test_data = get_test_data('bms_test_data.xlsx', 'memberCentre', 22)
        self.url = get_host('test') + self.test_data['url']
        self.payload = self.test_data['data']
        self.header = json.loads(self.test_data['header'])
        self.header['authorization'] = getBmsToken().get_token()
        self.method = self.test_data['method']
        self.databaseOperations = databaseOperations()

    def add_member_group(self):
        """
        bms-新增会员分组
        :return:
        """
        # 如果存在这个auto_test分组就先删除
        for i in self.databaseOperations.select_member_group():
            if 'auto_test' in i:
                self.databaseOperations.delete_member_group()
        try:
            resp = get_response(self.url, self.method, data=self.payload, headers=self.header)  # 未解密接口返回
            resp_str = getJsonStr(resp.json()['data']).get_json_str()  # 解密接口返回数据
            resp = resp.json()
            resp['data'] = resp_str['data']
            return resp
        except Exception as e:
            self.log.error('新增会员账户接口异常:{}，请检查'.format(str(e)))


if __name__ == '__main__':
   res = addMemberGroup().add_member_group()
   print(res)