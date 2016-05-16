'''
__init__()
魔法方法
这个方法在创建对象的时候，自动调用。
可以在这里初始化实例属性

实例对象，通过类创建的对象

self：表示当前实例对象
'''




class Dog:
	def eat(self):								
		print('dog...eat...self=%s'%self)

'''
此时wangcai叫实例对象
Dog叫类对象
'''
wangcai = Dog()
print(wangcai)
wangcai.eat()		

		

print('************************************华丽的分割线************************************')

'''
这种方式，表示
每次初始化（实例化）得到一个新的对象，属性都一致
'''
class Dog:
	def __init__(self):
		print('init...self=%s'%self)
		self.a = 'xx'
		self.b = 110

wangcai = Dog()
print(wangcai.a)
print(wangcai.b)


xiaoqiang = Dog()
print(xiaoqiang.a)
print(xiaoqiang.b)

print('************************************华丽的分割线************************************')

'''
在创建对象的时候，可以定制属性值
'''
class Dog:
	def __init__(self,name,age):
		print('init...self=%s'%self)
		self.a = name
		self.b = age

wangcai = Dog('旺财',3)
print(wangcai.a)
print(wangcai.b)


xiaoqiang = Dog('小强',2)
print(xiaoqiang.a)
print(xiaoqiang.b)


print('************************************华丽的分割线************************************')


'''
self.属性				叫实例属性
实例对象.属性			叫实例属性


__init__		
	在创建对象的时候，可以初始化属性
'''
class Dog:
	def __init__(self,name,age):
		print('init...self=%s'%self)
		self.name = name
		self.age = age

wangcai = Dog('旺财',3)
print(wangcai.name)
print(wangcai.age)
#wangcai.color = '黑色'


xiaoqiang = Dog('小强',2)
print(xiaoqiang.name)
print(xiaoqiang.age)


print('************************************华丽的分割线************************************')

class Dog:
	def __init__(self,name,age=1):
		print('init...self=%s'%self)
		self.name = name
		self.age = age

wangcai = Dog('旺财',3)
print(wangcai.name)
print(wangcai.age)
#wangcai.color = '黑色'


xiaoqiang = Dog('小强',2)
print(xiaoqiang.name)
print(xiaoqiang.age)


laowang = Dog('老王')
print(laowang.name)
print(laowang.age)
