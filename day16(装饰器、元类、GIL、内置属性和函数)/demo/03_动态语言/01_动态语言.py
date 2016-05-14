'''
	如果为一个类，增加类方法，首先准备一个类方法格式的方法

	如果为一个类，增加实例方法，首先准备一个实例方法格式的方法，
	然后使用Types模块的types.MethodType，给实例对象绑定实例方法
'''


class Person(object):
	def __init__(self, name = None, age = None):
		self.name = name
		self.age = age


xiaoming = Person("小明", "24")

#为实例对象增加实例属性
xiaoming.num=110

print(dir(xiaoming))

#为类增加类属性
Person.xx = 110
print(dir(Person))

print(xiaoming.xx)

#del Person.xx


def eat(self,food):
	print('%s 吃 %s'%(self.name,food))

@classmethod
def drink(cls):
	print(cls)

@staticmethod
def play():
    print("---static method----")



Person.eat = eat

print(dir(Person))

#Person.eat('饺子')


xiaoming = Person("小明", "24")
xiaoming.eat = eat
xiaoming.eat(xiaoming,'饺子')


print('***************************************华丽的分割线***************************************')

import types

xiaoming = Person("小明", "24")
xiaoming.eat = types.MethodType(eat,xiaoming)
xiaoming.eat('饺子')


xiaoming = Person("小明", "24")
#为实例对象增加实例方法
xiaoming.eat = types.MethodType(eat,xiaoming)
xiaoming.eat('饺子')

'''
TypeError: first argument must be callable

Person.drink = types.MethodType(drink,Person)
'''
#为类对象增加类方法
Person.drink = drink

Person.drink()

#为类对象增加静态方法
Person.play = play
Person.play()


print('***************************************华丽的分割线***************************************')
'''
	delattr
	del 
	只能删除类属性和对象属性，不能删除方法
'''

class Person(object):
	num = 110
	def __init__(self, name = None, age = None):
		self.name = name
		self.age = age
	def f1(self):
		print('f1...')
	@classmethod
	def f2(self):
		print('f2...')


del Person.f2
delattr(Person,'num')
#print(Person.num)


#laowang = Person('老王',20)
#delattr(laowang,'f1')
#del laowang.f1
#laowang.f1()


#xiaoqiang = Person('小强',20)
#xiaoqiang.f1()


laowang = Person('老王',20)
#del laowang.f1
#print(laowang.f1)


print('***************************************华丽的分割线***************************************')
'''
	__slots__只能限定实例属性、实例方法
'''


class Person(object):
	__slots__=('name','age')
	def __init__(self, name = None, age = None):
		self.name = name
		self.age = age

laowang = Person('x',10)
#laowang.xx = 110

#Person.num=10


def eat(self,food):
	print('%s 吃 %s'%(self.name,food))

@classmethod
def drink(cls):
	print(cls)

#laowang.eat = types.MethodType(eat,laowang)
#Person.eat = eat




'''
动态语言：
	在运行过程中，可以为对象增加减少属性、方法

非动态语言：
	一旦类确定了，后期不能修改
'''