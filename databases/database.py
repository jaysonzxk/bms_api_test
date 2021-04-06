"""
author： mask
filename: databases.py
datetime： 2021/3/26 10:35 
ide： PyCharm
"""
import pymysql
import datetime


# from interfaces.user_info import userInfo


class databaseOperations:
    def __init__(self):
        self.db = pymysql.connect('192.168.0.201', 'root', '123456', 'dev')
        self.cursor = self.db.cursor()
        self.date_today_start = datetime.datetime.today().strftime('%Y-%m-%d 00:00:00')
        self.date_today_end = datetime.datetime.today().strftime('%Y-%m-%d 23:59:59')
        # self.user_id = userInfo().get_user_info()['data']['userId']

    def select_user(self):
        """
        查询用户
        :return:
        """
        sql = "SELECT * FROM sys_user WHERE username = 'auto_test'"
        self.cursor.execute(sql)
        username = self.cursor.fetchall()
        return username

    def select_member_sum(self, operate):
        """
        查询数据sys_user所有用户
        :return:
        """
        sql = "SELECT count(1) FROM sys_user WHERE role_code = 'ROLE_FRONT' AND is_operate = {}".format(operate)
        self.cursor.execute(sql)
        user_sum = self.cursor.fetchall()[0][0]
        return user_sum

    def select_userid(self, name):
        """
        查询用户userid
        :return:
        """
        sql = "SELECT user_id FROM sys_user WHERE username = '{}'".format(name)
        self.cursor.execute(sql)
        user_id = self.cursor.fetchall()[0][0]
        return user_id

    def delete_user(self):
        """
        测试完成后，重置测试数据
        :return:
        """
        sql = "DELETE FROM sys_user WHERE username = 'auto_test'"
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except Exception as e:
            print(e)
            self.db.rollback()

    def select_bet_details(self):
        """
        查询彩票注单数量
        :return:
        """
        sql = """
                     select * from zx_lottery_bet_0 where user_id='556' union                 
                     select * from zx_lottery_bet_1 where user_id='556' union               
                     select * from zx_lottery_bet_2 where user_id='556' union                 
                     select * from zx_lottery_bet_3 where user_id='556' union                 
                     select * from zx_lottery_bet_4 where user_id='556' union                 
                     select * from zx_lottery_bet_5 where user_id='556' union                 
                     select * from zx_lottery_bet_6 where user_id='556' union                 
                     select * from zx_lottery_bet_7 where user_id='556' union                 
                     select * from zx_lottery_bet_8 where user_id='556' union                 
                     select * from zx_lottery_bet_9 where user_id='556'
                """
        self.cursor.execute(sql)
        data = self.cursor.fetchall()
        return len(data)

    def user_status_0(self):
        """
        获取用户状态(重置为0，未锁定状态)
        :return:
        """
        sql_select = "SELECT lock_flag FROM sys_user WHERE username = 'miya30000'"
        sql_update = "update sys_user set lock_flag = 0 WHERE username = 'miya30000'"
        self.cursor.execute(sql_select)
        status = self.cursor.fetchall()[0][0]
        if status == 1:
            self.cursor.execute(sql_update)
            self.db.commit()

    def user_status_1(self):
        """
        获取用户状态(重置为1，锁定状态)
        :return:
        """
        sql_select = "SELECT lock_flag FROM sys_user WHERE username = 'miya30000'"
        sql_update = "update sys_user set lock_flag = 1 WHERE username = 'miya30000'"
        self.cursor.execute(sql_select)
        status = self.cursor.fetchall()[0][0]
        if status == 0:
            self.cursor.execute(sql_update)
            self.db.commit()

    def select_bet_status(self):
        """
        查询会员投注状态(0禁止，1开启)
        :return:
        """
        sql_select = "SELECT is_bet FROM sys_user WHERE username = 'miya30000'"
        sql_update = "update sys_user set is_bet = 1 WHERE username = 'miya30000'"
        self.cursor.execute(sql_select)
        bet_status = self.cursor.fetchall()[0][0]
        if bet_status == 0:
            self.cursor.execute(sql_update)
            self.db.commit()

    def select_withdraw_status(self):
        """
        查询会员投注状态(0禁止，1开启)
        :return:
        """
        sql_select = "SELECT is_withdraw FROM sys_user WHERE username = 'miya30000'"
        sql_update = "update sys_user set is_withdraw = 1 WHERE username = 'miya30000'"
        self.cursor.execute(sql_select)
        bet_status = self.cursor.fetchall()[0][0]
        if bet_status == 0:
            self.cursor.execute(sql_update)
            self.db.commit()

    def select_fund_status(self):
        """
        查询会员资金状态(0开启，1冻结)
        :return:
        """
        sql_select = "SELECT is_fund_freeze FROM sys_user WHERE username = 'miya30000'"
        sql_update = "update sys_user set is_fund_freeze = 0 WHERE username = 'miya30000'"
        self.cursor.execute(sql_select)
        fund_status = self.cursor.fetchall()[0][0]
        if fund_status == 1:
            self.cursor.execute(sql_update)
            self.db.commit()

    def select_return_point_status(self):
        """
        查询会员返点状态(0禁止，1开启)
        :return:
        """
        sql_select = "SELECT is_return_point FROM sys_user WHERE username = 'miya30000'"
        sql_update = "update sys_user set is_return_point = 1 WHERE username = 'miya30000'"
        self.cursor.execute(sql_select)
        fund_status = self.cursor.fetchall()[0][0]
        if fund_status == 0:
            self.cursor.execute(sql_update)
            self.db.commit()

    def select_operate_status_0(self):
        """
        查询会员返点状态(0正式账号，1运营账号)
        :return:
        """
        sql_select = "SELECT is_operate FROM sys_user WHERE username = 'miya30000'"
        sql_update = "update sys_user set is_operate = 0 WHERE username = 'miya30000'"
        self.cursor.execute(sql_select)
        fund_status = self.cursor.fetchall()[0][0]
        if fund_status == 1:
            self.cursor.execute(sql_update)
            self.db.commit()

    def select_operate_status_1(self):
        """
        查询会员返点状态(0正式账号，1运营账号)
        :return:
        """
        sql_select = "SELECT is_operate FROM sys_user WHERE username = 'miya30000'"
        sql_update = "update sys_user set is_operate = 1 WHERE username = 'miya30000'"
        self.cursor.execute(sql_select)
        fund_status = self.cursor.fetchall()[0][0]
        if fund_status == 0:
            self.cursor.execute(sql_update)
            self.db.commit()

    def register_code_nums(self):
        """
        注册码
        :return:
        """
        sql = " SELECT count(1) FROM zx_user_register_code LIMIT 100000"
        self.cursor.execute(sql)
        code_nums = self.cursor.fetchall()[0][0]
        return code_nums

    def login_log_nums(self):
        """
        会员登录日志
        :return:
        """
        sql = " SELECT count(1) FROM zx_user_login_log LIMIT 100000"
        self.cursor.execute(sql)
        log_nums = self.cursor.fetchall()[0][0]
        return log_nums

# if __name__ == '__main__':
#     databaseOperations().select_withdraw_status()
