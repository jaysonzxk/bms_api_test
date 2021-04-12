"""
author： mask
filename: bms_login.py
datetime： 2021/3/19 0:25
ide： PyCharm
"""
import time

from common.base import get_response, get_host
from test_data.read_data import get_test_data
from common.logger import Log
import json


class getBmsToken(object):
    def __init__(self):
        self.test_data = get_test_data('bms_test_data.xlsx', 'login', 0)
        self.log = Log()
        self.url = get_host('test') + self.test_data['url']
        self.method = self.test_data['method']
        self.payload = self.test_data['data']
        self.header = json.loads(self.test_data['header'])

    def get_token(self):
        """
        获取bms登录token
        :return:token.txt
        """
        try:
            while True:
                resp = get_response(self.url, self.method,
                                    data=self.payload, headers=self.header)
                if resp.json().get('access_token'):
                    token = resp.json()['token_type'] + ' ' + resp.json()['access_token']
                    return token
        except Exception as e:
            self.log.error('获取token出现异常:{}，请检查登录接口请求'.format(str(e)))


if __name__ == '__main__':
    res = getBmsToken().get_token()
    print(res)
