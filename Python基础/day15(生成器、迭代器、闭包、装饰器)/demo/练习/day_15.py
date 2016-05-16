#将内容保存到列表

ls1 = list(range(10))
print(ls1)

ls2 = [x*5 for x in range(10)]
print(ls2)

#生成器V1.0

ge = (x*2 for x in range(100))
print(ge)
print(type(ge))

print("****************************************************")

j = 0
for i in ge:
	if j == 99:
		print(i)
	j+=1
print("****************************************************")

#生成器V2.0
#将计算结果添加到列表中
def fib(times):
	ls = []
	n = 0
	a,b = 0,1
	while n<times:
		ls.append(b)
		a,b = b,a+b
		n+=1
	return ls
print(fib(10))
print("****************************************************")
#将计算结果挨个输出
def fib(times):
	n = 0
	a,b = 0,1
	while n<times:
		print(b,end=",")
		a,b = b,a+b
		n+=1
	return "done"
print(fib(10))
print("****************************************************")

#生成器V2.0

#yield的用法
#函数没有执行，而是返回一个生成器对象
def fib(times):
	print("begin...")
	n = 0
	a,b = 0,1
	while n < times:
		print("1....")
		yield b
		print("2....")
		a, b = b ,a+ b
		n+=1
	print("end....")
ge = fib(10)
print(ge)

#使用next()输出

def fib(times):
	print("begin...")
	n = 0
	a,b = 0,1
	while n < times:
		print("1....")
		yield b
		print("2....")
		a, b = b ,a+ b
		n+=1
	print("end....")
ge = fib(10)
a = next(ge)
print(a)
print("分隔线")
a = next(ge)
print(a)
print("分隔线")
a = next(ge)
print(a)
print("分隔线")
a = next(ge)
print(a)
print("****************************************************")
#或者循环输出
for i in ge:
	print(i)
print("****************************************************")
#函数的send的传递

def fib(times):
	print("begin...")
	n = 0
	a,b = 0,1
	while n < times:
		print("1...")
		temp = yield b
		print("temp:%s"%temp)
		print("2...")
		a,b = b,a+b
		n+=1
	print("end...")
ge = fib(5)

print(next(ge))
print(next(ge))
print(next(ge))

print("****************************************************")

#第一次使用next
#以后使用send，功能等于next
#send目的就是可以动态传递参数，来改变算法
ge = fib(6)
next(ge)
print(ge.send("老王"))

print("****************************************************")

def getNums(start,end):
	for i in range(start,end):
		temp = yield None
		if temp:
			if i%2==0:
				print("sdhfgujk%s"%i)
		else:
			if i%2!=0:
				print("ja%s"%i)
ge = getNums(1,20)
next(ge)
print(ge.send(True))
print(ge.send(True))
print(ge.send(True))
print(ge.send(False))
print(ge.send(False))
print(ge.send(False))

print("****************************************************")

#send模拟多任务
"""
def test1():
	while True:
		print("111111111111111")
		yield None

def test2():
	while True:
		print("222222222222222")
		yield None
t1 = test1()
t2 = test2()
while True:
	t1.__next__()
	t2.__next__()
"""
print("****************************************************")
#生成器
ls = [110,119,120]

it = iter(ls)
print(it)
print(next(it))
print(next(it))
print(next(it))

ls = {110,119,120}

it = iter(ls)
print(it)
print(next(it))
print(next(it))
print(next(it))
print("****************************************************")
#判断是不是可迭代
import collections
from collections import Iterable,Iterator
print(isinstance(tuple(),Iterable))
print(isinstance(dict(),Iterable))
print(isinstance(list(),Iterable))
print(isinstance("",Iterable))
print(isinstance(set(),Iterable))
print(isinstance(range(100),Iterable))
print(isinstance((x for x in range(10)),Iterable))
print("****************************************************")
#判断是不是迭代器
print(isinstance(tuple(),Iterator))
print(isinstance(list(),Iterator))
print(isinstance(set(),Iterator))
print(isinstance(dict(),Iterator))
print(isinstance("",Iterator))
print(isinstance(range(10),Iterator))
print(isinstance((x for x in range(10)),Iterator))

#闭包的引用

def one(a,b):
	def two(c):
		return a*c + b
	return two
la = one(2,3)
print(la(3))

#类也能完成

class m():
	def __init__(self,a,b):
		self.a = a
		self.b = b
	def sa(self,c):
		return self.a*c+self.b
sasa = m(2,3)
print(sasa.sa(3))

print("*************************************************")
#装饰器

def a(func):
	print("a函数的输出语句!!!")
	def b():
		print("b函数开始语句!!!")
		func()
		print("b函数结束语句!!!")
	return b
def save():
	print("保存")

ret = a(save)
ret()

print("*************************************************")

def a(func):
	print("a函数的输出语句!!!")
	def b():
		print("b函数开始语句!!!")
		func()
		print("b函数结束语句!!!")
	return b
@a
def save():
	print("保存")

save()

print("***************利用装饰器来解决登录问题*****************")
"""
#利用装饰器来解决登录问题

def panduan(func):
	def a():
		name = input("请输入您的名字:")
		pwd = input("请输入密码:")
		if name=="laowang" and pwd=="123":
			func()
		else:
			print("输入错误，请重新输入!!!")
	return a

@panduan
def save():
	print("保存成功!!!")
save()
"""
#自己利用装饰器写

def a(fun):
	print("闭包的开始")
	def b():
		name = input("请输入您的名字:")
		pwd = input("请输入密码:")
		if name == "1" and pwd == "1":
			print("登陆成功")
			fun()
		else:
			print("登录失败，账号或者密码错误!!!")
	return b
@a
def c():
	print("保存成功!!!")
c()


