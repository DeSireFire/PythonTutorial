'''
class Dog:
	pass

wangcai = Dog()
wangcai()

报错
AttributeError: Dog instance has no __call__ method
Dog对象不能被调用
'''


'''
__call__魔法方法，当对象()的自动调用


class Dog:
	def __call__(self):
		print('call...')

wangcai = Dog()
wangcai()
'''


class Test(object):

	def __init__(self, func):
		print("---初始化---")
		print("func name is %s"%func.__name__)
		self.__func = func

	def __call__(self):
		print("---在这里写装饰器中的功能---")
		self.__func()


@Test
def foo():
	print("I am foo")

#print(foo)

'''
调用者
'''
foo()

'''
	此时@Test做了哪些事？

	1、foo = Test(foo)
	2、自动执行__init__
'''


'''
魔法方法：

	__new__
	__init__
	__str__
	__del__
	__call__
'''