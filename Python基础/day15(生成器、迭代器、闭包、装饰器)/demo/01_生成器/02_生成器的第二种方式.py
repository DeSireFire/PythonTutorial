


'''
def fib(times):
	ls = []
	n = 0
	a,b = 0,1
	while n<times:
		#print(b)
		ls.append(b)
		a,b = b,a+b
		n+=1
	return ls
'''


'''
def fib(times):
	n = 0
	a,b = 0,1
	while n<times:
		print(b)
		a,b = b,a+b
		n+=1
	return 'done'

ret = fib(5)
print(ret)
'''

'''
生成器的第二种方式:

1、定义函数
2、函数yield 值
'''

def fib(times):
	print('begin...')
	n = 0
	a,b = 0,1
	while n<times:
		print('1...')
		yield b
		print('2...')
		a,b = b,a+b
		n+=1
	print('end...')

'''
函数并没有调用执行，返回一个生成器对象
'''
ge = fib(5)					
print(ge)


'''
next(generator)
执行算法，到yield到结束，将yield之后的值最为返回值 返回。

如果next并没有取到yield后的值。报错StopIteration。

Traceback (most recent call last):
  File "D:\work\python\2017-07-17\讲课\day15\demo\01_生成器\02_生成器的第二种方式.py", line 7
    ret1 = next(ge)
StopIteration

'''
ret1 = next(ge)
print(ret1)

ret1 = next(ge)
print(ret1)

ret1 = next(ge)
print(ret1)

ret1 = next(ge)
print(ret1)

ret1 = next(ge)
print(ret1)

print('***************************************华丽的分割线***************************************')

ge = fib(5)

for i in ge:
	print(i)


print('***************************************华丽的分割线***************************************')


'''
生成器的第二种方式:

为算法传递参数send

send只能yield开始的代码
'''

def fib(times):
	print('begin...')
	n = 0
	a,b = 0,1
	while n<times:
		print('1...')
		temp = yield b
		print('temp=%s'%temp)
		print('2...')
		a,b = b,a+b
		n+=1
	print('end...')


ge = fib(5)
print(next(ge))
print(next(ge))

print('***************************************华丽的分割线***************************************')


'''
	第一次使用next
	以后使用send，功能==next的功能
'''

ge = fib(5)
next(ge)
ge.send('老王')
ge.send('老王')


print('***************************************华丽的分割线***************************************')

'''
send的目的就是可以动态传递参数，来改变算法
'''
def getNums(begin,end):
	for i in range(begin,end):
		temp = yield None
		if temp:
			#模拟业务逻辑算法1
			if i%2==0:
				print('....%s'%i)
		else:
			#模拟业务逻辑算法2
			if i%2==1:
				print('....%s'%i)


ge = getNums(1,20)

next(ge)

ret = ge.send(True)


print('***************************************华丽的分割线***************************************')

'''
send模拟多任务,了解，不用写代码
'''


'''
def test1():
	while True:
		print("--1--")
		yield None

def test2():
	while True:
		print("--2--")
		yield None


t1 = test1()
t2 = test2()
while True:
	t1.__next__()
	t2.__next__()
'''


print('***************************************华丽的分割线***************************************')

def test1():
	while True:
		print("--1--")


def test2():
	while True:
		print("--2--")



t1 = test1()
t2 = test2()






