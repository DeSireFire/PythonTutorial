'''
	在函数中，不能直接修改全局变量
	如果需要修改，需要使用global
'''

num = 100
def f():
	global num
	num = num+1
	print('f...num=%s'%num)
f()
print(num)



def f():
	global a
	a = 100

f()
print(a)
