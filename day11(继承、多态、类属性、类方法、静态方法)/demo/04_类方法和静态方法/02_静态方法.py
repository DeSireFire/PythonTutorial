'''

	静态方法：
		语法：普通函数的格式，不需要强制要求传递参数。在方法的头部加注解(装饰器)@staticmethod
				一般用于与实例对象、类对象无关的内容
	
		调用：
			实例对象可以调用
			类对象可以调用
'''

class Dog:
	
	def run(self):
		print('run...self=%s'%self)

	@classmethod
	def stop(cls):
		print('stop...cls=%s,id(cls)=%s'%(cls,id(cls)))

	@staticmethod
	def prepare():
		print('prepare...')

	@staticmethod
	def f1(num):
		print('num=%s'%(num))
		print(Dog)


d = Dog()
d.prepare()

Dog.prepare()


d.f1(100)

