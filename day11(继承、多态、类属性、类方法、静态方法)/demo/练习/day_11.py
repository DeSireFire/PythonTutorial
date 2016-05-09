'''
class Fu():

	def __init__(self):
		self.__name = "立方尽快"
	def __ha(self):
		print("哈哈…………")
	def getname(self):
		return self.__name

class zi(Fu):

	def getname2(self):
		return self.__name

cl = zi()
print(cl.getname2)
ll = cl.getname
print(ll)

print("&&&&&&&&&&&&&&&&&&&&&&&&&&&")

class Fu():
	def __init__(self):
		print("Fu ;';;;;")
		self.num = 20
	def sayHello(self):
		print("Fu hello******")
class Zi(Fu):
	def __init__(self):
		print("Zi ::::::")
		self.num = 1004
	def sayHello(self):
		print("Zi hello******")
	#改变指针
	def sayhaha(self):
		print("haha>>>>1")
	def sayhaha(self):
		print("haha>>>>2")
la = Zi()
la.sayHello()
print(la.num)
print(la.sayhaha())
	
print("*************************************************")

class a1:
	def hah(self):
		print("haha1haha1haha1haha1haha1haha1haha1")
class a2:
	def hah(self):
		print("haha2haha2haha2haha2haha2haha2haha2")
class a3(a1,a2):
	def hah(self):
		print("haha3haha3haha3haha3haha3haha3haha3")
cl = a3()
cl.hah()
print(a3.__mro__)

print("*************************************************")

class a1:
	def hah(self):
		print("haha1haha1haha1haha1haha1haha1haha1")
class a2:
	def hah(self):
		print("haha2haha2haha2haha2haha2haha2haha2")
class a3(a1,a2):
	def hah(self):
		print("haha3333333333")
		a2.hah(self)
		super().hah()
k = a3()
k.hah()
print(a3.__mro__)

print("*************************************************")

class Fu():
	def k(self,name):
		print("nihao%s"%name)
class Zi(Fu):
	def k(self):
		super().k("老王")
		print("hsdjkh")
l = Zi()
l.k()

print("*************************************************")

class Fu():
	def __init__(self,name,age):
		self.name = name
		self.age = age
class Zi(Fu):
	def __init__(self,sex,name,age):
		self.sex = sex
		self.name = name
		self.age = age
		#super().__init__(self,name,age)
		

ll = Zi("女","小红",20)
print(ll.name)
print(ll.age)
print(ll.sex)

print("*************************************************")

class Fu():
	def __init__(self,name,age):
		self.name = name
		self.age = age
class Zi(Fu):
	def __init__(self,sex,name,age):
		self.sex = sex
		super().__init__(name,age)
		

ll = Zi("女","小丽",19)
print(ll.name)
print(ll.age)
print(ll.sex)

print("*************************************************")

class Fu():
	def __init__(self,name,age):
		self.name = name
		self.age = age
		self.address = "北京"
class Zi(Fu):
	def __init__(self,sex,name,age):
		self.sex = sex
		Fu.__init__(self,name,age)
		

ll = Zi("男","小王",19)
print(ll.name)
print(ll.age)
print(ll.sex)
print(ll.address)
print("*************************************************")

class Animal():
	def __init__(self,name):
		self.name = name
		self.color = "白色"
	

class dog(Animal):
	def __init__(self,name):
		super().__init__(name)
	def getname(self):
		return self.name
wangcai = dog("旺财")
print(wangcai.name)
print(wangcai.color)
'''
'''
#实例属性与类属性
class animal():
	def __init__(self,name,color):
		self.name = name
		self.color = color
	def f(self,num):
		self.num = num
d = animal("老李子","白色")
d.sex = "男"
d.f(1000)
print(isinstance(d,animal))
print(dir(d))


class dog:
	#类属性
	name = "旺财"
	type = "啸天犬"
	def run(self):
		print("我正在跑…………")
d1 = dog()
d2 = dog()
print(d1.name)
print(d2.name)
d1.name="老王"
print(d1.name)
print(d2.name)
dog.name = "老李"
print(d1.name)
print(d2.name)

print("******************************************************")

class Dog:
	#类属性
	name = "旺财"
	type = "啸天犬"
	def run(self):
		print("我正在跑…………")
#改变指向，随意定义了一个方法，self可以是任意的，不一定是self
def stop(self):
	print("我要休息，不跑了!!!!")

d1 = Dog()
d2 = Dog()

Dog.stop = stop
print(Dog.stop)
print(stop)

d1.stop()
print(id(d1.stop))
print(id(d2.stop))
print(id(Dog.stop))

Dog.run = stop
d1.run()
'''
class Dog:
	def run(self):
		print("run......self=%s"%self)
	@classmethod
	def stop(cls):
		print("stop.....cls=%s,id(cls)=%s"%(cls,id(cls)))
	@classmethod
	def f1(cls,num):
		cls.num = num

wangcai = Dog()
wangcai.run()
wangcai.stop()

print(wangcai)
print(Dog())
print(id(Dog))

Dog.stop()
Dog.f1(120)
print(Dog.num)

#静态方法
print("**********************************************************")
class Dog():
	def run(self):
		print("run......self=%s"%self)
	@classmethod
	def stop(cls):
		print("stop.....cls=%s,id(cls)=%s"%(cls,id(cls)))
	@staticmethod
	def prepare():
		print("我是静态方法!!!!")
	@staticmethod
	def f1(num):
		print("num=%s"%num)
		print(Dog)
		
d = Dog()
d.prepare()

Dog.prepare()
d.f1(130)

print("**************************************************************")

class People():

	country = "china"

	@staticmethod
	def getCountry():
		return People.country
print(People.getCountry())

print("**************************************************************")

class People():

	country = "china"
	__num = 100
	#定义一个类方法
	@classmethod
	def getCountry(cls):
		print(type(cls))
		print(cls)
		return cls.country

	#定义一个静态方法
	@staticmethod
	def myStaticMethod():
		print("我的一个静态方法!!!")
		print(People.__num)

p = People()
p.country = 1
print(p.getCountry())
print(People.getCountry())

p.myStaticMethod()
People.myStaticMethod()
print("***********************************************************")


