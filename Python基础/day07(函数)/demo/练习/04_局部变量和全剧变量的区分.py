'''
	局部变量和全局变量
	局部变量就是定义在函数内部的变量,
		局变量能调用全局变量但是，无法修改全局变量
			如果在函数中修改全局变量，那么就需要使用global进行声明
	全局变量就是定义在函数外边的变量

	如果全局变量的名字和局部变量的名字相同，那
		么使用的是局部变量

'''
# 局部变量和全剧变量的区分
num = 100
def la(m):
	m+=100
	print('函数内部使用的结果是:%s'%m)
la(num)
print(num)

num = 100
def la():
	global num
	num+=100
	print('函数内部使用的结果是:%s'%num)
la()
print(num)

num = 100
def la(m):
	m+=100
	print('函数结果是:%s'%m)
la(145)
print(num)

num1=1000
def la():
	
	print('函数内部使用的结果是:%s'%num1)
la()
print(num1)

