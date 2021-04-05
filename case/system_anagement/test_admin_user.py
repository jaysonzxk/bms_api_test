"""
author： mask
filename: test_admin_user.py
datetime： 2021/4/5 11:08 
ide： PyCharm
"""
import unittest
from ddt import data, ddt
from common.logger import Log
from interfaces.admin_user import adminUser
from common.get_expect_data import get_expect


@ddt
class testAdminUser(unittest.TestCase, adminUser):

    @classmethod
    def setUpClass(cls) -> None:
        cls.log = Log()
        cls.data = adminUser().test_data

    @data(*(get_expect('bms_test_data.xlsx', 'systemManagement', 0)))
    def test_admin_user(self, test_data):
        """
        测试获取bms后台管理用户信息接口
        :param test_data:
        :return:
        """
        res = adminUser().get_admin_user()
        results = [res['code'], res['msg']]
        self.log.info('----------测试开始----------')
        self.log.info('测试场景：[{}]'.format(self.data['module']))
        self.log.info('测试断言-->期望值/校验值[{}]'.format(test_data))
        self.log.info('测试断言-->实际值[{}]'.format(res))
        self.log.info('请求参数:{}'.format(self.data['data']))
        self.log.info('请求接口:{}'.format(adminUser().url))
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