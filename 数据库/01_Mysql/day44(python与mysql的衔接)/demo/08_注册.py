from pymysql import *
from datetime import *
from hashlib import *

class MysqlHelper():
    """封装操作mysql的功能"""
    def __init__(self,host,port,db,user,passwd,charset='utf8'):
        """初始化参数"""
        self.host=host
        self.port=port
        self.db=db
        self.user=user
        self.passwd=passwd
        self.charset=charset
    def connect(self):
        """获取连接对象和工具对象"""
        self.conn = connect(host=self.host, port=self.port, db=self.db, user=self.user, passwd=self.passwd,charset=self.charset)
        self.cursor = self.conn.cursor()
    def close(self):
        """关闭"""
        self.cursor.close()
        self.conn.close()

    def __edit(self,sql,params=None):
        """增删改"""
        self.cursor.execute(sql,params)
        self.conn.commit()

    def insert(self,sql,params=None):
        self.__edit(sql,params)
    def delete(self,sql,params=None):
        self.__edit(sql,params)
    def update(self,sql,params=None):
        self.__edit(sql,params)

    def select_one(self,sql,params=None):
        """查询单个"""
        self.cursor.execute(sql, params)
        return self.cursor.fetchone()

    def select_all(self, sql, params=None):
        """查询多个"""
        self.cursor.execute(sql, params)
        return self.cursor.fetchall()


def mymd5(value):
    my_md5 = md5()
    my_md5.update(value.encode('utf-8'))
    return  my_md5.hexdigest()

def mysha1(value):
    pass

def register():
    username = input('输入用户名：')
    userpwd = input('输入密码：')
    userpwd = mymd5(userpwd)

    helper = MysqlHelper('localhost', 3306, 'laowang', 'root', 'root')
    helper.connect()
    sql = ''
    params = []
    helper.insert(sql,params)
    helper.close()

    print('哦了......')
