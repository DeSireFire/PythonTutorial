'''
无参，无返(return None)

def 函数名():
	语句
'''

def f1():
	for i in range(1,11):
		print(i)

f1()
ret = f1()
print(ret)

print('****************************华丽的分割线****************************')
'''
有参，无返

def 函数名(形参1,形参2...):
	语句
'''


def add(a,b):		
	a = a+b
	print(a)

num1 = 1
num2 = 2

add(num1,num2)		#a,b = num1,num2
print(num1)


def add(a,b):
	a = a+b			#重新赋值，改变指针

num1 = [1,2,3]
num2 = [4,5]
add(num1,num2)
print(num1)


def add(a,b):
	a.append(b)		#修改，没有改变指针

num1 = [1,2,3]
num2 = [4,5]
add(num1,num2)	#a,b = num1,num2
print(num1)


print('****************************华丽的分割线****************************')

'''
	无参，有返

	def 函数名():
		语句
		return 值


	return有两个功能：
		1、return 值    结束函数，并返回值
		2、return       结束函数，不返回值---返回None
		只要函数中出现return 函数结束
'''


def f1():
	num = 0
	for i in range(1,11):
		num+=i
	return num


ret = f1()
print(ret)


def f2():
	print('1...')
	return 110
	print('2...')

f2()

'''
flag = True
while flag
	while
		while
			while
				while
					if xx:
						flag = False
						break



def f():
	while 
		while
			while
				while
					while
						if xx:
							return
'''
print('****************************华丽的分割线****************************')
'''
	有参，有返

	这里的start,end叫形参
	调用的时候，传递的值，比如1，101是实参
'''
def f1(start,end):
	print('begin...')
	num = 0
	for i in range(start,end):
		num+=i
	return num

ret = f1(1,101)
print(ret)


