from pymysql import *

try:
    conn = connect(host='localhost',port=3306,db='laowang',user='root',passwd='root',charset='utf8')
    cur = conn.cursor()
    cur.execute('delete from c2 where id=1')
    conn.commit()
    conn.close()
except OperationalError:
    print('连接失败')
except Exception:
    conn.rollback()
    conn.close()


