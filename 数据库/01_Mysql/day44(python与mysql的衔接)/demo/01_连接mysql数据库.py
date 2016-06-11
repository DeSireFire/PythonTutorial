from pymysql import *


# 连接数据库,获取连接对象
conn = connect(host='localhost',port=3306,db='laowang',user='root',passwd='root',charset='utf8')

# 获取Cursor对象,执行工具
cur = conn.cursor()

#执行sql语句,执行增删改,返回的是受影响的行数
cur.execute('delete from c2 where id=1')

#提交
conn.commit()

#关闭连接
conn.close()
