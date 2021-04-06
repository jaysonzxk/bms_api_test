"""
author： mask
filename: test_fund_freeze.py
datetime： 2021/4/6 15:31 
ide： PyCharm
"""
import unittest
from ddt import data, ddt
from common.logger import Log
from databases.database import databaseOperations
from interfaces.fund_freeze import fundFreeze
from common.get_expect_data import get_expect


@ddt
class testFundFreeze(unittest.TestCase, fundFreeze):

    @classmethod
    def setUpClass(cls) -> None:
        cls.log = Log()
        cls.data = fundFreeze().test_data
        cls.log.info('正在初始化数据库测试数据。。。。。。')
        databaseOperations().select_fund_status()

    @data(*(get_expect('bms_test_data.xlsx', 'memberCentre', 13)))
    def test_disable_bet(self, test_data):
        """
        测试资金冻结接口
        :param test_data:
        :return:
        """
        res = fundFreeze().fund_freeze()
        results = [res['code'], res['msg']]
        self.log.info('----------测试开始----------')
        self.log.info('测试场景：[{}]'.format(self.data['module']))
        self.log.info('测试断言-->期望值/校验值[{}]'.format(test_data))
        self.log.info('测试断言-->实际值[{}]'.format(res))
        self.log.info('请求参数:{}'.format(self.data['data']))
        self.log.info('请求接口:{}'.format(fundFreeze().url))
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
        Log().info('正在重置数据库测试数据。。。。。。')
        databaseOperations().select_fund_status()


if __name__ == '__main__':
    unittest.main()