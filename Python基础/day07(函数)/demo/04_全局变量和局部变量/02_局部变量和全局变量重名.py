
'''

	局部变量作用范围：
		只有在函数中有效。函数调用结束，局部变量就无法访问了。

	在函数中，访问变量，如果自己有，不会访问函数之外的全局变量
'''
num = 100
def f(num):
	num+=100
	print('f...num=%s'%num)
f(num)
print(num)


