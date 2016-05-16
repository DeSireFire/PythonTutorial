'''
	函数的嵌套：
		函数里再调用其它函数
'''

def f1():
	print('f1...begin')
	f2()
	print('f1...end')

def f2():
	print('f2...begin')
	print('f2...end')

f1()


def f1(a,b):
	print('f1...begin')
	f2(a+b)
	print('f1...end')

def f2(num1):
	print('f2...begin')
	print('num1=%s'%num1)
	print('f2...end')

f1(1,2)


