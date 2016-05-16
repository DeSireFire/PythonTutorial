'''

	可变：		列表、字典、set
	不可变：	数字、字符串、元组、布尔、空



	如果是不可变类型，传递之后。互不影响。
	如果是可变类型，传递之后
		1、如果是修改，不改变指向，影响原来的值
		2、如果是修改，改变指向，不影响原来的值
'''




def f(ls):
	ls.append(110)
	print('ls=%s'%ls)

a = [1,2,3]
f(a)
print('a=%s'%a)


def f(ls):
	ls = 110
	print('ls=%s'%ls)

a = [1,2,3]
f(a)
print('a=%s'%a)


def f(num):
	num = 110
	print('num=%s'%num)

a = 120
f(a)
print('a=%s'%a)
