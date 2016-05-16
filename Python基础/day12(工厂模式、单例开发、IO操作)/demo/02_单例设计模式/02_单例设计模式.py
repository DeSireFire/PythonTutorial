'''
	单例模式？
		在项目中，有一些对象，使用了很长时间，或者这个对象贯穿整个项目。
		创建这个对象，需要运行很多代码，占用很长时间和资源。
		所以一般这样的对象，可以设计成单例模式，只创建一次。
		


	原型模式？
		每次创建都是新的对象，python默认就是如此。
'''

class Singleton:
	__instance = None
	def __new__(*args,**kwargs):
		if args[0].__instance==None:
			args[0].__instance = object.__new__(args[0])
		return args[0].__instance



s1 = Singleton()
s2 = Singleton()
print(s1==s2)

















class Singleton:
	__instance = None
	__firstInit = True					#True 第一次调用    False: 不是第一次

	def __init__(self,name):
		print('__init__...')
		if self.__firstInit:
			self.name = name
			self.__firstInit = False

	def __new__(*args,**kwargs):
		if args[0].__instance==None:
			args[0].__instance = object.__new__(args[0])
		return args[0].__instance



s1 = Singleton('老王')
s2 = Singleton('旺财')

print(s1.name)
print(s2.name)

