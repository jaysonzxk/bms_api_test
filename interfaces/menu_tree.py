"""
author： mask
filename: menu_tree.py
datetime： 2021/4/5 12:15 
ide： PyCharm
"""
from common.base import get_response, get_host
from test_data.read_data import get_test_data
from common.logger import Log
from common.bms_login import getBmsToken
from common.tojsonstr import getJsonStr
import json


class menuTree:
    """
    系统管理-菜单管理
    """

    def __init__(self):
        self.log = Log()
        self.test_data = get_test_data('bms_test_data.xlsx', 'systemManagement', 3)
        self.url = get_host('test') + self.test_data['url']
        self.header = json.loads(self.test_data['header'])
        self.header['authorization'] = getBmsToken().get_token()
        self.method = self.test_data['method']

    def get_menu_tree(self):
        """
        获取bms后台菜单
        :return:
        """
        try:
            resp = get_response(self.url, self.method, headers=self.header)  # 未解密接口返回
            resp_str = getJsonStr(resp.json()['data']).get_json_str()  # 解密接口返回数据
            resp = resp.json()
            resp['data'] = resp_str['data']
            return resp
        except Exception as e:
            self.log.error('获取bms后台菜单接口异常:{}，请检查'.format(str(e)))


# if __name__ == '__main__':
#     res = menuTree().get_menu_tree()
#     print(res)