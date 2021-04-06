"""
author： mask
filename: test_user_bet_details.py
datetime： 2021/4/6 11:34 
ide： PyCharm
"""
import unittest
from ddt import data, ddt
from common.logger import Log
from interfaces.get_user_bet_details import userBetDetails
from common.get_expect_data import get_expect


@ddt
class testUserBetDetails(unittest.TestCase, userBetDetails):

    @classmethod
    def setUpClass(cls) -> None:
        cls.log = Log()
        cls.data = userBetDetails().test_data

    @data(*(get_expect('bms_test_data.xlsx', 'memberCentre', 7, keyword='bet_details')))
    def test_user_bet_details(self, test_data):
        """
        测试获取会员注单详情接口
        :param test_data:
        :return:
        """
        res = userBetDetails().get_user_bet_details()
        results = [res['data']['total'], res['code'], res['msg']]
        self.log.info('----------测试开始----------')
        self.log.info('测试场景：[{}]'.format(self.data['module']))
        self.log.info('测试断言-->期望值/校验值[{}]'.format(test_data))
        self.log.info('测试断言-->实际值[{}]'.format(res))
        self.log.info('请求参数:{}'.format(self.data['data']))
        self.log.info('请求接口:{}'.format(userBetDetails().url))
        self.log.info('请求方法:{}'.format(self.data['method']))
        self.log.info('响应结果:{}'.format(res))
        self.assertIn(test_data, results, msg='测试不通过，失败原因：%s not in %s' %
                                              (test_data, results))
        self.log.info('测试断言[{}]通过'.format(test_data))
        self.log.info('----------测试通过----------')
        self.log.info('----------测试结束----------')
        self.log.info('=======================================================')

    @classmethod
    def tearDownClass(cls):
        pass


if __name__ == '__main__':
    unittest.main()