'''
定义类的语法：

	class 类名:
		def 方法名(self,形参1,形参2...):
			语句

	类名命名方式：大驼峰
	注意：
		1、控制缩进
		2、类名以后有冒号

	self：表示当前实例对象


	每次创建都是一个新的对象
'''

#创建类
class Car:
	def run(self):
		print('car run...')
	def stop(self):
		print('car stop...')

#创建对象
mini = Car()
mini.run()
mini.stop()

print(Car.run)
print(mini.run)


c1 = Car()
c2 = Car()
print(id(c1))
print(id(c2))


#为对象添加属性

c1 = Car()
c1.run()
c1.stop()

c1.brand = '特斯拉'
c1.color='金黄'

print(c1.brand)
print(c1.color)

c1.brand = '比亚迪'
print(c1.brand)


'''
c2 = Car()
print(c2.brand)
'''

'''
del c1.brand
print(c1.brand)
'''
