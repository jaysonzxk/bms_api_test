"""
author： mask
filename: test_disable_return_point.py
datetime： 2021/4/6 15:37 
ide： PyCharm
"""
import unittest
from ddt import data, ddt
from common.logger import Log
from databases.database import databaseOperations
from interfaces.open_return_point import openReturnPoint
from common.get_expect_data import get_expect


@ddt
class testOpenReturnPoint(unittest.TestCase, openReturnPoint):

    @classmethod
    def setUpClass(cls) -> None:
        cls.log = Log()
        cls.data = openReturnPoint().test_data
        cls.log.info('正在初始化数据库测试数据。。。。。。')
        databaseOperations().select_return_point_status()

    @data(*(get_expect('bms_test_data.xlsx', 'memberCentre', 15)))
    def test_open_return_point(self, test_data):
        """
        测试开启会员返点接口
        :param test_data:
        :return:
        """
        res = openReturnPoint().open_return_point()
        results = [res['code'], res['msg']]
        self.log.info('----------测试开始----------')
        self.log.info('测试场景：[{}]'.format(self.data['module']))
        self.log.info('测试断言-->期望值/校验值[{}]'.format(test_data))
        self.log.info('测试断言-->实际值[{}]'.format(res))
        self.log.info('请求参数:{}'.format(self.data['data']))
        self.log.info('请求接口:{}'.format(openReturnPoint().url))
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
        databaseOperations().select_return_point_status()


if __name__ == '__main__':
    unittest.main()