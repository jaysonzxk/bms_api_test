"""
author： mask
filename: test_unlock_user.py
datetime： 2021/4/6 14:24 
ide： PyCharm
"""
import unittest
from ddt import data, ddt
from common.logger import Log
from databases.database import databaseOperations
from interfaces.unlock_user import unlockUser
from common.get_expect_data import get_expect


@ddt
class testUnlockUser(unittest.TestCase, unlockUser):

    @classmethod
    def setUpClass(cls) -> None:
        cls.log = Log()
        cls.data = unlockUser().test_data
        cls.log.info('正在初始化数据库测试数据。。。。。。')
        databaseOperations().user_status_1()

    @data(*(get_expect('bms_test_data.xlsx', 'memberCentre', 10)))
    def test_unlock_user(self, test_data):
        """
        测试解锁会员账号接口
        :param test_data:
        :return:
        """
        res = unlockUser().unlock_user()
        results = [res['code'], res['msg']]
        self.log.info('----------测试开始----------')
        self.log.info('测试场景：[{}]'.format(self.data['module']))
        self.log.info('测试断言-->期望值/校验值[{}]'.format(test_data))
        self.log.info('测试断言-->实际值[{}]'.format(res))
        self.log.info('请求参数:{}'.format(self.data['data']))
        self.log.info('请求接口:{}'.format(unlockUser().url))
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
        databaseOperations().user_status_1()


if __name__ == '__main__':
    unittest.main()