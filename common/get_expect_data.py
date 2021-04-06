"""
author： mask
filename: get_expect_data.py
datetime： 2021/3/20 11:33 
ide： PyCharm
"""


from test_data.read_data import get_test_data
from databases.database import databaseOperations
import json


def get_expect(*args, keyword=None, operate=None, game_type=None, expect_name='expect'):
    """
    动态获取期望值，
    :param args: 元组：测试文件路径，sheet名称，数字n
    :param expect_name: 表格头部key
    :param keyword: 数据库查询字段
    :param operate: 数据库查询字段 是否是正式账号还是运营账号
    :param game_type: 查询的游戏类型
    :return:
    """
    expect = json.loads(get_test_data(*args).get(expect_name))
    expect_list = []
    if keyword == 'user_sum':
        # 查询用总数
        res = databaseOperations().select_member_sum(operate)
        expect_list.append(res)
    elif keyword == 'bet_details':
        # 查询游戏注单总数
        res = databaseOperations().select_bet_details()
        expect_list.append(res)
    if len(expect) > 1:
        for key, value in expect.items():
            expect_list.append(value)
    return expect_list


# if __name__ == '__main__':
#     res = get_expect('bms_test_data.xlsx', 'memberCentre', 0, keyword='user_sum')
#     print(res)