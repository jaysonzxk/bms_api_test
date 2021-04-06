"""
author： mask
filename: test_cancel_is_operate.py
datetime： 2021/4/6 15:57 
ide： PyCharm
"""
import unittest
from ddt import data, ddt
from common.logger import Log
from databases.database import databaseOperations
from interfaces.cancel_is_operate import cancelIsOperate
from common.get_expect_data import get_expect


@ddt
class testCancelIsOperate(unittest.TestCase, cancelIsOperate):

    @classmethod
    def setUpClass(cls) -> None:
        cls.log = Log()
        cls.data = cancelIsOperate().test_data
        cls.log.info('正在初始化数据库测试数据。。。。。。')
        databaseOperations().select_operate_status_1()

    @data(*(get_expect('bms_test_data.xlsx', 'memberCentre', 17)))
    def test_cancel_is_operate(self, test_data):
        """
        测试设置正式账号接口
        :param test_data:
        :return:
        """
        res = cancelIsOperate().cancel_is_operate()
        results = [res['code'], res['msg']]
        self.log.info('----------测试开始----------')
        self.log.info('测试场景：[{}]'.format(self.data['module']))
        self.log.info('测试断言-->期望值/校验值[{}]'.format(test_data))
        self.log.info('测试断言-->实际值[{}]'.format(res))
        self.log.info('请求参数:{}'.format(self.data['data']))
        self.log.info('请求接口:{}'.format(cancelIsOperate().url))
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
        databaseOperations().select_operate_status_0()


if __name__ == '__main__':
    unittest.main()