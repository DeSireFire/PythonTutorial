#partial偏函数,会返回一个新的函数
#把一个函数的某些参数设置默认值

import functools

def show(*args,**kwargs):
	print(args)
	print(kwargs)

p1 = functools.partial(show,2,3,4,5)
p1()
p1(6,7,8,9)
p1(a="laowang",b="laoli")
# (2, 3, 4, 5)
# {}
# (2, 3, 4, 5, 6, 7, 8, 9)
# {}
# (2, 3, 4, 5)
# {'b': 'laoli', 'a': 'laowang'}

print("**********************************************************")

#wraps函数,消除副作用

#普通装饰器
def a(func):
	"a function"
	def b():
		"b function"
		print("a something")
		return func()
	return b
@a
def c():
	"c function"
	print("I am c")
c()
print(c.__doc__)
#结果:
# a something
# I am c
# b function

print("**********************************************************")

#使用wraps函数消除副作用
def a(func):
	"a function"
	@functools.wraps(func)
	def b():
		"b function"
		print("a something")
		return func()
	return b
@a
def c():
	"c function"
	print("I am c")
c()
print(c.__doc__)
#结果:
# a something
# I am c
# c function

print("**********************************************************")

# 常用模块time
import time

print(time.time())#时间戳
print(time.ctime())#当地时间
t1 = time.localtime()
print(type(t1))#<class 'time.struct_time'>
#获取具体某个时间
print(t1.tm_year)
print(t1.tm_mon)
print(t1.tm_mday)
print(t1.tm_hour)
print(t1.tm_min)
print(t1.tm_sec)
#获取当地时间年月日
print(time.strftime("%Y-%m-%d"))#2017-08-09
#获取当地时间年月日 时分秒
print(time.strftime("%Y-%m-%d %H:%M:%S"))#2017-08-09 14:11:44
#将时间元组以指定的格式转换为字符串形式。接受字符串格式化串、时间元组。
#时间元组为可选，默认为localtime()

print("**********************************************************")
#指定时间的访问和设置
#指定时间必须是九位数字
t = (2015,2,22,16,25,55,0,0,0)
print(t)
t = time.mktime(t)#将本地时间元组转换为时间戳。接受一个时间元组
print(t)
t = time.gmtime(t)#返回时间组
#time.struct_time(tm_year=2015, tm_mon=2, tm_mday=22, tm_hour=8, tm_min=25, tm_sec=55, tm_wday=6, tm
#yday=53, tm_isdst=0)
print(t)

t1 = time.strftime("%Y-%m-%d %H:%M:%S",t)#返回具体的时间点时区-8的时间
#2015-02-22 08:25:55
print(t1)
t2 = time.strftime("%Y-%m-%d %H:%M:%S",(2015,2,22,16,25,55,0,0,0))#返回具体的时间点
#2015-02-22 16:25:55
print(t2)

print("**********************************************************")
#日期时间
import datetime

d1 = datetime.datetime(2016,8,9,10,57,46)
print(d1.year)#获取具体年份

d1 = datetime.datetime(2015,5,6)
print(d1)
d11 = d1.strftime("%Y/%m/%d")
print(d11)

d1 = datetime.datetime.now()
print(d1)#获取当前时间的所有时间点2017-08-09 13:34:17.155052
t1 = d1.strftime("%Y*%m*%d")#获取当前时间2017*08*09
print(t1)

tt = "2017/8/8"
ta = "%Y/%m/%d"
dda = datetime.datetime.strptime(tt,ta)
#将指定格式的时间字符串解析为时间元组，strftime()的逆向过程。
#接受字符串，时间格式2个参数，都是必选。
print(dda)#2017-08-08 00:00:00
print(type(dda))#<class 'datetime.datetime'>



print("**********************************************************")

#加密md5(hashli)
import hashlib

m = hashlib.md5()#创建加密算法，得到一个128位密文
print(m)#<md5 HASH object>得到一个hash object对象地址
		#<md5 HASH object @ 0x00000000006F24B8>

a = "lao"
m.update(a.encode("utf-8"))#更新哈希对象，以字符串参数

print(m.hexdigest())#返回十六进制数字字符串

print("**********************************************************")

#自学sha模块的加密
#sha+数字就是加密级别，数字越大，加密得到的越复杂

k = hashlib.sha1()
print(k)
aa = "laowang"
k.update(aa.encode("utf-8"))
print(k.hexdigest())

k = hashlib.sha256()
print(k)
aa = "laowang"
k.update(aa.encode("utf-8"))
print(k.hexdigest())

k = hashlib.sha384()
print(k)
aa = "laowang"
k.update(aa.encode("utf-8"))
print(k.hexdigest())

k = hashlib.sha512()
print(k)
aa = "laowang"
k.update(aa.encode("utf-8"))
print(k.hexdigest())
# <sha1 HASH object @ 0x0000000000692710>
# 84b80208564fc0eb0a73f89a9a05811d338f04ba
# <sha256 HASH object @ 0x000000000122D878>
# 6501d36787b6877067d82f5325916b6e6ecda6c7948acb4b15d212ae66d1f180
# <sha384 HASH object @ 0x0000000000692710>
# 8381944f38ceb8ff149386ef8e651201c3142e8f8ca811a7c1a9387d5e3210ac227ff1b26959d9c8a0cb8e3fdc14df08
# <sha512 HASH object @ 0x000000000122D878>
# b5faf70633b95296650e22bc77830e5b8b79fbcd740ea8205e9b5b827df4a5ef881be52cd27a61ad56897c3cbd0e0385281
# 9a533d1f972545ca5515638e563e
# 
