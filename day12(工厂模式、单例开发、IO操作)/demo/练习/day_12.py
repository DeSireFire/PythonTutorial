'''
class Animal():
	def a(self):
		pass
	def b(self):
		pass

class a1(Animal):
	def a(self):
		print("动物一在叫。。。")
	def b(self):
		print("动物一在睡觉。。。")
	print("我是第一个")
	print("*******************************************")

class a2(Animal):
	def a(self):
		print("动物二在叫。。。")
	def b(self):
		print("动物二在睡觉。。。")
	print("我是第二个")
	print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

class Factory:
	@classmethod
	def alll(cls,name):
		ret = None
		if name == 'a1':
			ret = a1()
		elif name == 'a2':
			ret = a2()
		return ret

#函数式编程，一般不建议使用，建议使用面向对象方式创建
def creat(name):
	ret = None
	if name == 'a1':
		ret = a1()
	elif name == "a2":
		ret = a2()
	return ret
def main():
	animal = creat("a1")
	animal.a()
	animal.b()

def main():
	b1 = Factory.alll('a1')
	print(b1)
	b1.a()
	b1.b()
main()
'''

#单例模式
class A:
	def __init__(self,name,age):
		self.name = name
		self.age = age

	def __new__(cls,name,age):
		m = super().__new__(cls)
		return m
a = A("老王",20)
print(a)

print("*********************************************")

#解决多参数问题
class A:
	def __init__(self,name,age):
		self.name = name
		self.age = age

	def __new__(cls,*args,**kwargs):
		m = super().__new__(cls)
		return m
a = A("老王",20)
b = A("老李",10)
print(a)
print(b)

print("*********************************************")

#解决多参数问题，并且不需修改
class A:
	def __init__(self,name,age,l):
		print(self)
		print("$$$$$$$$$$")
		self.name = name
		self.age = age

	def __new__(cls,*args,**kwargs):
		print(cls)
		print(args)
		print(kwargs)
		m = super().__new__(cls)
		return m
a = A("老王",20,l = "10")
b = A("老李",10,l="111")
print(a)
print(b)

print("*********************************************")

#解决多参数问题，最终
class A:
	def __init__(self,name,age,l):
		print(self)
		print("$$$$$$$$$$")
		self.name = name
		self.age = age

	def __new__(*args,**kwargs):
		print(args)
		print(kwargs)
		m = object.__new__(args[0])
		return m
a = A("老王",20,l = "10")
b = A("老李",10,l="111")
print(a)
print(b)

print("*********************************************")

#解决多参数问题，最终
class B:
	__la = None
	__he = True
	def __init__(self,name):
		if self.__he:
			self.name = name
			self.__he = False

	def __new__(*args,**kwargs):
		if args[0].__la == None:
			args[0].__la = object.__new__(args[0])
		return args[0].__la

a = B("老王")
print(a.name)
b = B("老李")
print(a.name)
print(b.name)

print("*********************************************")

#解决多参数问题，最终
class B:
	__la = None
	def __init__(self,name):	
		self.name = name
	def __new__(*args,**kwargs):
		if args[0].__la == None:
			args[0].__la = object.__new__(args[0])
		return args[0].__la

a = B("老王")
print(a.name)
b = B("老李")
print(a.name)
print(b.name)



print("*********************************************")

#单例模式
class A:
	__la = None
	def __new__(*args,**kwargs):
		if args[0].__la == None:
			args[0].__la = object.__new__(args[0])
		return args[0].__la
a = A()
b = A()
print(a==b)

#文件读
'''
f = open(r"C:\Users\Administrator\Desktop\Noname2.txt","r",encoding="utf-8")
m = f.read()
f.close()
'''

print("*********************************************")

#工厂实例
class made_in_china:
	def made(self):
		print("中国制造!!!")

class made_in_henan(made_in_china):
	def made(self):
		print("河南制造!!!")

class made_in_henbei(made_in_china):
	def made(self):
		print("河北制造!!!")

#创建工厂类
class Factory:
	@classmethod
	def made_in_factory(cls,name):
		ret = None
		if name == "nan":
			ret = made_in_henan()
		elif name == "bei":
			ret = made_in_henbei()
		return ret

def main():
	made_in = Factory.made_in_factory("nan")
	made_in.made()

#程序入口
main()

#单例模式
class singleton_pattern:
	__sp = None
	def __new__(*args,**kwargs):
		if not args[0].__sp:
			args[0].__sp = object.__new__(args[0])
		return args[0].__sp
a = singleton_pattern()
b = singleton_pattern()
print(a)
print(b)
print(id(a))
print(id(b))
print(a==b)
