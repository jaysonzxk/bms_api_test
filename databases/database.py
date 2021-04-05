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

    def select_admin_user(self):
        """
        查询后台用户
        :return:
        """
        sql = "SELECT * FROM sys_user WHERE username = 'auto_test'"
        self.cursor.execute(sql)
        username = self.cursor.fetchall()
        return username

    def select_admin_userid(self):
        """
        查询后台管理用户userid
        :return:
        """
        sql = "SELECT user_id FROM sys_user WHERE username = 'admin'"
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