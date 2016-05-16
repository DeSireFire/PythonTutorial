'''
	实例方法：
		语法：
			必须有一个参数，这个参数表示当前实例对象，一般是self
		调用：
			只能通过实例对象调用


	类方法：
		语法：
			必须有一个参数，这个参数表示当前类对象，一般是cls。在方法的头部加注解(装饰器)@classmethod
		调用：
			实例对象可以调用
			类对象可以调用


	实例属性：
				1、实例对象.属性 = 值


	类属性：  
				1、类对象.属性 = 值
				2、定义在类内部，方法外部

	
'''

class Dog:

	def run(self):
		print('run...self=%s'%self)

	@classmethod
	def stop(cls):
		print('stop...cls=%s,id(cls)=%s'%(cls,id(cls)))

	@classmethod
	def f1(cls,num):
		cls.num = num
		#Dog.num = num


wangcai = Dog()
wangcai.run()
wangcai.stop()

print(wangcai)
print(Dog)
print(id(Dog))

Dog.stop()

Dog.f1(10)
print(Dog.num)




