import time


print(time.time())
print(time.ctime())
#time.sleep(2)
t1 = time.localtime()
print(type(t1))
print(t1.tm_year)
print(t1.tm_mon)
print(t1.tm_mday)
print(t1.tm_hour)
print(t1.tm_min)
print(t1.tm_sec)


t2 = time.strftime('%Y-%m-%d')
print(t2)

t2 = time.strftime('%Y-%m-%d %H:%M:%S')
print(t2)
print('************************************华丽的分割线************************************')

t = (2009, 2, 17, 17, 3, 38,  0,0,0)
print(t)
t = time.mktime(t)
print(t)
t = time.gmtime(t)
print(t)

t2 = time.strftime('%Y-%m-%d %H:%M:%S',t)
print(t2)

t2 = time.strftime('%Y-%m-%d %H:%M:%S',(2009, 2, 17, 17, 3, 38,  0,0,0))
print(t2)



#time.struct_time(tm_year=2009, tm_mon=2, tm_mday=17, tm_hour=9, tm_min=3, tm_sec=38, tm_wday=1, tm_yday=48, tm_isdst=0)

from datetime import datetime
from time import strftime


print('************************************华丽的分割线************************************')
d1 = datetime(2017,8,9,10,57,46)
print(str(d1))
print(dir(d1))
print(d1.year)

print('************************************华丽的分割线************************************')
d1 = datetime(2017,8,9)
print(d1)
t1 = d1.strftime('%Y/%m/%d')
print(t1)
print('************************************华丽的分割线************************************')
d1 = datetime.now()
print(d1)
t1 = d1.strftime('%Y/%m/%d')
print(t1)

print('************************************华丽的分割线************************************')

t1 = '2017/08/09'
format = '%Y/%m/%d'
d1 = datetime.strptime(t1,format)
print(str(d1))
print(type(d1))