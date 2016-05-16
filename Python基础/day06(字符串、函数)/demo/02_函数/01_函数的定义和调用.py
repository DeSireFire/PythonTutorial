'''
	讲解的是函数
'''

a = 100
b = 200
ret = a
if ret<b:
	ret = b
print(ret)


def getMax(a,b):
	ret = a
	if ret<b:
		ret = b
	return ret

#print(getMax(1,2))
#print(getMax(10,22))


def eat():
	print('eat的功能。。。。。。')

def drink():
	print('drink的功能。。。。。。')


def f():
	print('eat的功能。。。。。。')
	print('drink的功能。。。。。。')


print('****************************华丽的分割线****************************')


'''
	语法：
		def 函数名(形参1,形参2,形参3...):
			语句1
			语句2
			...
			return 值


	注意：
		1、函数名符合标识符的要求，小驼峰
		2、小括号，参数根据要求，可以写也可以不写
		3、小括号后有冒号
		4、注意缩进
		5、return 根据需要。可以写也可以不写
			如果调用函数，运行完毕之后，想返回一个值，使用return 
			不想返回，就不写。相当于return None

	函数分为
		1、定义
			其实就相当于变量
		2、调用
			记得加小括号
'''

print('begin...')


#函数的定义
def haha():
	print('哈哈')
	print('呵呵')

print('end...')
#函数的调用:找到变量haha指向的函数，执行
haha()
print(haha)
print(haha())


haha = 123
print(haha)
#print(haha())

print('****************************华丽的分割线****************************')


def haha():
	print('哈哈')


def haha():
	'''
		haha()
		输出'haha'
	'''
	print('haha')

haha()


