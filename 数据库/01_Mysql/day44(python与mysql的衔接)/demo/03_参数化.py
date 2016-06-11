from pymysql import *

con = connect("host='192.168.14.85',port=3306,db='day41',user='root',passwd='root',charset='utf8'")

cur = con.cursor()

a = [222,'lala',200]

num = cur.execute('insert into user(id,name,money) VALUES(%s,%s,%s)',a)

if num>0:
    print("sucess")
else:
    print("default")

con.commit()
con.close()