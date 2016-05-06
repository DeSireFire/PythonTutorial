'''
	面向对象技术简介
	类(Class): 用来描述具有相同的属性和方法的对象的集合。
				它定义了该集合中每个对象所共有的属性和方法。对象是类的实例。
	类变量：类变量在整个实例化的对象中是公用的。
				类变量定义在类中且在函数体之外。类变量通常不作为实例变量使用。
	数据成员：类变量或者实例变量用于处理类及其实例对象的相关的数据。
	方法重写：如果从父类继承的方法不能满足子类的需求，
				可以对其进行改写，这个过程叫方法的覆盖（override），也称为方法的重写。
	实例变量：定义在方法中的变量，只作用于当前实例的类。
	继承：即一个派生类（derived class）继承基类（base class）的字段和方法。
				继承也允许把一个派生类的对象作为一个基类对象对待。
				例如，有这样一个设计：一个Dog类型的对象派生自Animal类，
				这是模拟"是一个（is-a）"关系（例图，Dog是一个Animal）。
	实例化：创建一个类的实例，类的具体对象。
	方法：类中定义的函数。
	对象：通过类定义的数据结构实例。对象包括两个数据成员（类变量和实例变量）和方法。
'''
'''
class Car:
	#self表示当前实例对象
	#实例变量：定义在方法中的变量，只作用于当前实例的类
	#self: 代表类的实例，self 在定义类的方法时是必须有的，
	#      虽然在调用时不必传入相应的参数。
	def runing(self):
		print("我是别克，我在跑………………")
	def toot(self):
		print("我在按喇叭鸣笛………………")

bb = Car()
bb.color = '白色'
bb.lunzi = '四驱动'
bb.runing()
bb.toot()
print('汽车属性:',bb.color,end = '')
print(bb.lunzi)
print()
bb.color = '黑色'
bb.lunzi = '涡轮四驱'
print('汽车属性:',bb.color,end = '')
print(bb.lunzi)
print()
print('********************************')
print()
bb1 = Car()
bb1.color = '金黄色'
bb1.lunzi = '二区'
bb1.runing()
bb1.toot()
print('汽车属性:',bb1.color,end = '')
print(bb1.lunzi)
'''
class Car():
	def __init__(self):
		self.name = '福特'
		self.price = 486748
dazhong = Car()
print(dazhong.name)
print(dazhong.price)

print('************************************************')

class Car():
	def __init__(self,name,price):
		self.name = name
		self.price = price
dazhong = Car('一汽大众',120000)
print(dazhong.name)
print(dazhong.price)

print('************************************************')

print()
print('自定义参数，然后覆盖与没参数时的自动调用本身')
print()
class Car():
	def __init__(self,name='本田',price=10000):
		self.name = name
		self.price = price
dazhong = Car('一汽大众',120000)
print(dazhong.name)
print(dazhong.price)

fute = Car('福特')
print(fute.name)
print(fute.price)

class Car():
	def __init__(self,name,price=10000):
		print(self)
		self.name = name
		self.price = price
dazhong = Car('一汽大众',120000)
print(dazhong)
print(dazhong.name)
print(dazhong.price)

fute = Car('福特',321545)
print(fute)
print(fute.name)
print(fute.price)
print('************************************************')

print()
print('多参数调用，元组和字典的使用')
print()

class Car():
	def __init__(self,*name,**price):
		print(self)
		self.name = name
		self.price = price
dazhong = Car('一汽大众',la='塞班',p=1544)
print(dazhong)
print(dazhong.name)
print(dazhong.price)

fute = Car('福特','别克','奥迪',lala = '小米',sasa = '雷军',papa=321545)
print(fute)
print(fute.name)
print(fute.price)
print('************************************************')

