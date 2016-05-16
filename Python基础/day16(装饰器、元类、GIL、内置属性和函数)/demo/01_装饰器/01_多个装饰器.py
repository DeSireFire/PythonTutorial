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
'''
save头部加@outer，python解析器做了哪些事？
save = outer(save)
'''


'''
多个装饰器顺序。

先开始，后结束
'''

#定义函数：完成包裹数据
def makeBold(fn):
	def wrapped():
		return "<b>" + fn() + "</b>"
		#return 'xx'
	return wrapped

#定义函数：完成包裹数据
def makeItalic(fn):
	def wrapped():
		return "<i>" + fn() + "</i>"
	return wrapped

@makeBold
def test1():
	return "hello world-1"

@makeItalic
def test2():
	return "hello world-2"




@makeBold
@makeItalic
def test3():
	return "hello world-3"

print(test1())
print(test2())

print('***************************************华丽的分割线***************************************')

print(test3())



