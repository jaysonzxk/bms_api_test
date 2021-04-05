"""
author： mask
filename: edit_user_info.py
datetime： 2021/4/5 16:17 
ide： PyCharm
"""
from common.base import get_response, get_host
from test_data.read_data import get_test_data
from common.logger import Log
from interfaces.user_info import getUserInfo
from common.bms_login import getBmsToken
from common.tojsonstr import getJsonStr
import json


class editUserInfo:
    """
    会员中心--修改用户资料
    """

    def __init__(self):
        self.log = Log()
        self.test_data = get_test_data('bms_test_data.xlsx', 'memberCentre', 3)
        self.url = get_host('test') + self.test_data['url']
        self.data = json.dumps(getUserInfo().get_user_info()['data'])
        self.header = json.loads(self.test_data['header'])
        self.header['authorization'] = getBmsToken().get_token()
        self.method = self.test_data['method']

    def edit_user_info(self):
        """
        获取bms后台修改用户资料
        :return:
        """
        if 'false' not in self.data:
            self.data.replace('true', 'false')
        else:
            self.data.replace('false', 'true')
        try:
            resp = get_response(self.url, self.method, data=self.data, headers=self.header)  # 未解密接口返回
            resp_str = getJsonStr(resp.json()['data']).get_json_str()  # 解密接口返回数据
            resp = resp.json()
            resp['data'] = resp_str['data']
            return resp
        except Exception as e:
            self.log.error('bms后台获取用户资料接口异常:{}，请检查'.format(str(e)))


# if __name__ == '__main__':
#     res = editUserInfo().edit_user_info()
#     print(res)