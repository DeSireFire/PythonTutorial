'''
	子类和父类都有相同的属性、方法

	子类对象在调用的时候，会覆盖父类的，调用子类的

	与参数无关，只看名字

	覆盖、重写：
		扩展功能
'''
class Fu(object):
	def __init__(self):
		print('init1...')
		self.num = 20

	def sayHello(self):
		print("halou-----1")


class Zi(Fu):
	def __init__(self):
		print('init2...')
		self.num = 200
	def sayHello(self):
		print("halou-----2")

	
	'''
	改变指针
	def sayHaha(self):
		print("haha-----1")
	def sayHaha(self):
		print("haha-----2")
	'''


zi = Zi()
zi.sayHello()
print(zi.num)

print(Zi.__mro__)



print('*****************************************华丽的分割线*****************************************')


class C1:
	def haha(self):
		print('C1...haha')

class C2:
	def haha(self):
		print('C2...haha')

class C3(C1,C2):
	def haha(self):
		print('C3...haha')


c3 = C3()
c3.haha()

print(C3.__mro__)


print('*****************************************华丽的分割线*****************************************')

'''
super() 这个super类的对象，可以在子类中，找到父类的属性、方法。
并不是直接的父类对象
'''

class Fu(object):
	def sayHello(self):
		print("halou-----1...self=%s"%self)


class Zi(Fu):
	def sayHello(self):
		print("halou-----2...self=%s"%self)
		#super(Zi,self).sayHello()
		#super().sayHello()
		Fu.sayHello(self)
		print('super=%s...super()=%s...id(super())=%s'%(super,super(),hex(id(super()))))


zi = Zi()
zi.sayHello()

print(zi)

print('*****************************************华丽的分割线*****************************************')

class Fu1(object):
	def sayHello(self):
		print("halou-----fu1")

class Fu2(object):
	def sayHello(self):
		print("halou-----fu2")


class Zi(Fu1,Fu2):
	def sayHello(self):
		print("halou-----zi")
		#super().sayHello()
		Fu2.sayHello(self)

		


zi = Zi()
zi.sayHello()


print('*****************************************华丽的分割线*****************************************')
class Fu(object):
	def sayHello(self,name):
		print("halou-----fu")
	

class Zi(Fu):
	def sayHello(self):
		super().sayHello('老王')
		print("halou-----zi")


zi = Zi()
zi.sayHello()
#zi.sayHello('xxx')


print('*****************************************华丽的分割线*****************************************')

'''
class Fu(object):
	def __init__(self,name,age):
		self.name = name
		self.age = age
	

class Zi(Fu):
	def __init__(self,sex,name,age):
		self.sex = sex
		self.name = name
		self.age = age

zi = Zi('女','老王',20)
print(zi.name)
print(zi.age)
print(zi.sex)
'''

class Fu(object):
	def __init__(self,name,age):
		self.name = name
		self.age = age
	

class Zi(Fu):
	def __init__(self,sex,name,age):
		self.sex = sex
		#super().__init__(name,age)
		Fu.__init__(self,name,age)
		

zi = Zi('女','老王',20)
print(zi.name)
print(zi.age)
print(zi.sex)