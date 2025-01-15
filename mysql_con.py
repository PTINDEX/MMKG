# @Author: PT
# @CreateTime: 2024-06-05
# @Description:连接Mysql数据库、数据的增删改查、关闭数据库
# @Version:1.0

# 需导入的包
import pymysql

class Mysql(object):
    # 连接数据库
    def __init__(self):
        try:
            self.db = pymysql.connect(host="localhost", user="root", password="PT_mysql", database="xltjdb")
            #游标对象
            self.cursor = self.db.cursor()
            print("连接成功！")
        except:
            print("连接失败！")
    
    # 查询数据
    def get_one_data(self, username, password):
        # 加 binary 则区分大小写
        sql = "select* from accounts where binary username='" + username + "' and password ='" + password + "';"
        self.cursor.execute(sql)
        count = self.cursor.rowcount
        return count
    
    # 插入数据 
    def insertdata(self, username, email, password):
        # 用户名和邮箱均为唯一标识
        # 查询是否已存在用户名相同的用户
        sql = "select* from accounts where binary username = '" + username + "';"
        self.cursor.execute(sql)
        count = self.cursor.rowcount
        if count == 0:
            # 查询是否已存在邮箱相同的用户
            sql_email = "select* from accounts where binary email = '" + email + "';"
            self.cursor.execute(sql_email)
            count_email = self.cursor.rowcount
            if count_email == 0:
                sql = "insert into accounts(username, email, password)values('%s','%s','%s');" % (username, email, password)
                try:
                    self.cursor.execute(sql)
                    self.db.commit()
                except:
                    # 如果发生错误就回滚，建议使用这样发生错误就不会对表数据有影响
                    self.db.rollback()
        return
    
    # 更新数据
    def updatedata(self, username, new_pwd):
        # 先判断新密码和旧密码是否相同，取出该用户的密码
        sql = "select password from accounts where binary username = '" + username + "';"
        self.cursor.execute(sql)
        # 只取返回结果元组的第一个元素，str
        pwd = self.cursor.fetchone()[0]
        if pwd != new_pwd:
            sql = "update accounts set password = '" + new_pwd + "' where binary username = '" + username + "';"
            try:
                self.cursor.execute(sql)
                self.db.commit()
            except:
                self.db.rollback()
        return 
    
    # 重置密码
    def resetpwd(self, username, email, new_pwd, confirm_pwd):
        # 先判断用户名和email是否正确且匹配
        sql = "select* from accounts where binary username = '" + username + "' and email = '" + email + "';"
        self.cursor.execute(sql)
        count = self.cursor.rowcount
        if count > 0:
            # 存在该用户，可重置密码
            # 先判断新密码和旧密码是否相同，取出该用户的密码
            sql = "select password from accounts where binary username = '" + username + "';"
            self.cursor.execute(sql)
            # 只取返回结果元组的第一个元素，str
            pwd = self.cursor.fetchone()[0]
            if pwd == new_pwd:
                # 相同
                flag_reset = 2
            else:
                # 判断新密码和确认密码是否相同
                if new_pwd == confirm_pwd:
                    # 重置密码
                    flag_reset = 1
                    sql = "update accounts set password = '" + new_pwd + "' where binary username = '" + username + "';"
                    try:
                        self.cursor.execute(sql)
                        self.db.commit()
                    except:
                        self.db.rollback()
                else:
                    # 新密码和确认密码不同
                    flag_reset = 3           
        else:
            # 不存在该用户
            flag_reset = 0
        return flag_reset

    #关闭
    def __del__(self):
        self.db.close()
