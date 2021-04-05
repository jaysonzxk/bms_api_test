"""
author： mask
filename: get_expect_data.py
datetime： 2021/3/20 11:33 
ide： PyCharm
"""


from test_data.read_data import get_test_data
from databases.database import databaseOperations
import json


def get_expect(*args, keyword=None, expect_name='expect'):
    """
    动态获取期望值，
    :param args: 元组：测试文件路径，sheet名称，数字n
    :param expect_name: 表格头部key
    :param keyword: 数据库查询字段
    :return:
    """
    expect = json.loads(get_test_data(*args).get(expect_name))
    expect_list = []
    if keyword == 'username':
        # 查询用户名
        res = databaseOperations().select_userid()
        expect_list.append(res)
    elif keyword == 'plan_id':
        # 查询用户计划id
        databaseOperations().select_plan_detail()
    elif keyword == 'income':
        # 查询当日余额
        res = databaseOperations().select_user_income()
        expect_list.append(res)
    elif keyword == 'rewards':
        res = databaseOperations().select_user_rewards()
        expect_list.append(res)
    elif keyword == 'agent':
        res = databaseOperations().select_agent_total()
        expect_list.append(res)
    else:
        if len(expect) > 1:
            for key, value in expect.items():
                expect_list.append(value)
    return expect_list


# if __name__ == '__main__':
#     res = get_expect('app_test_data.xlsx', 'personalcenter', 2, keyword='income')
#     print(res)