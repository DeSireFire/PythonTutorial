from pymysql import *


# 连接数据库,获取连接对象
conn = connect(host='localhost',port=3306,db='laowang',user='root',passwd='root',charset='utf8')

# 获取Cursor对象,执行工具
cur = conn.cursor()

#执行sql语句,执行增删改,返回的是受影响的行数,执行查询,返回的是查询的数据的个数
cur.execute('select empno,ename,job,mgr,hiredate,sal,comm,deptno from EMP where empno = %s',[7369])
#ret = cur.execute('select empno,ename,job,mgr,hiredate,sal,comm,deptno from EMP')
#print(ret)

#处理数据
ret = cur.fetchone()
print('姓名:%s,日期:%s'%(ret[1],ret[4]))


#提交
conn.commit()

#关闭连接
conn.close()
