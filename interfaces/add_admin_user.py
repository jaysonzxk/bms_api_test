"""
author： mask
filename: add_admin_user.py
datetime： 2021/4/5 11:20 
ide： PyCharm
"""
from common.base import get_response, get_host
from test_data.read_data import get_test_data
from common.logger import Log
from databases.database import databaseOperations
from common.bms_login import getBmsToken
from common.tojsonstr import getJsonStr
import json
import datetime


class addAdminUser:
    """
    系统管理-新增后台管理用户
    """

    def __init__(self):
        self.log = Log()
        self.test_data = get_test_data('bms_test_data.xlsx', 'systemManagement', 1)
        self.url = get_host('test') + self.test_data['url']
        self.payload = json.loads(self.test_data['data'])
        self.header = json.loads(self.test_data['header'])
        self.header['authorization'] = getBmsToken().get_token()
        self.method = self.test_data['method']

    def add_admin_user(self):
        """
        新增bms后台管理用户
        :return:
        """
        if databaseOperations().select_admin_user():
            databaseOperations().delete_user()
        try:
            resp = get_response(self.url, self.method, data=json.dumps(self.payload), headers=self.header)  # 未解密接口返回
            resp_str = getJsonStr(resp.json()['data']).get_json_str()  # 解密接口返回数据
            resp = resp.json()
            resp['data'] = resp_str['data']
            return resp
        except Exception as e:
            self.log.error('新增bms后台管理用户接口异常:{}，请检查'.format(str(e)))


# if __name__ == '__main__':
#     res = addAdminUser().add_admin_user()
#     print(res)