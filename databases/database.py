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


# if __name__ == '__main__':
#     res = databaseOperations().select_admin_userid()
#     print(res)