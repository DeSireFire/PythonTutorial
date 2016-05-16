#### 第一波 ####
def foo():
    print('foo')

#foo     #表示是函数
foo()   #表示执行foo函数

#### 第二波 ####
def foo():
    print('foo')

foo = lambda x: x + 1

#foo()   # 执行下面的lambda表达式，而不再是原来的foo函数，因为foo这个名字被重新指向了另外一个匿名函数

print(foo(1))




'''
xx.java --编译-->  xx.class  ----> 运行
'''

print('***************************************华丽的分割线***************************************')

'''

def outer(func):
	print('1...func=%s'%(id(func)))
	def inner():
		print('2...')
		func()
		print('3...')
	return inner


def save():
	print('do save...')


def delete():
	print('do delete...')


ret = outer(save)
ret()

print(id(save))
'''



def outer(func):
	print('1...')
	def inner():
		print('2...')
		func()
		print('3...')
	return inner

@outer
def save():
	print('do save...')


'''
save头部加@outer，python解析器做了哪些事？
save = outer(save)
'''
save()

print('***************************************华丽的分割线***************************************')


def outer(func):
	def inner():
		print('登录中。。。')
		name = input('输入用户名：')
		pwd = input('输入密码：')
		if name=='laowang' and pwd=='12345':
			func()
		else:
			print('登录失败，不能执行后面的操作，请去重新登录')
	return inner


@outer
def save():
	print('do save...')


def delete():
	print('do delete...')


'''
调用
'''
#save()
delete()


'''

装饰器，功能就是在运行原来功能基础上，加上一些其它功能，比如权限的验证，比如日志的记录等等。
不修改原来的代码，进行功能的扩展。
'''