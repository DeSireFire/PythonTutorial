#装饰器
#普通装饰器V1.0
def a(func):
	def lala():
		print("开始!")
		func()
	return lala
@a
def b():
	print("b函数")
b()

print("**********************************************")
#多个装饰器嵌套V2.0

def a(func):
	def lala():
		return "A" + func() +"A"	
	return lala
def c(func):
	def la():
		return "B" + func() +"B"
	return la
@a
@c
def b():
	return "b函数"
print(b())

print("**********************************************")

#多个装饰器无参数V3.0

from time import ctime

def a(func):
	def lala():
		print("开始!%s"%func.__name__,ctime())
		func()
	return lala
@a
def b():
	print("b函数")
b()
print("**********************************************")

#多个装饰器有参数V4.0

from time import ctime

def a(func):
	def lala(aaa,bbb):
		print("开始!%s"%func.__name__,ctime())
		func(aaa,bbb)
	return lala
@a
def b(aa,bb):
	print("b函数计算结果是:%s"%(aa+bb))
b(2,9)

print("**********************************************")

#多个装饰器多个可变参数V5.0

from time import ctime

def a(func):
	def lala(*args,**kwargs):
		print("开始!%s"%func.__name__,ctime())
		func(*args,**kwargs)
	return lala
@a
def b(aa,bb):
	print("b函数计算结果是:%s"%(aa+bb))
b(24,9)
@a
def b(aa,bb,cc,dd):
	print("b函数计算结果是:%s"%(aa+bb+cc+dd))
b(24,9,78,45)


print("**********************************************")

#多个装饰器必须要有返回值V6.0

from time import ctime

def a(func):
	def lala(*args,**kwargs):
		
		return func(*args,**kwargs)

	return lala
@a
def b(aa,bb):
	return("b函数计算结果是:%s"%(aa+bb))
print(b(24,9))
@a
def b(aa,bb,cc,dd):
	return("b函数计算结果是:%s"%(aa+bb+cc+dd))
print(b(24,9,78,45))

print("**********************************************")

#扩展myself

def a(func):
	def lala(*args,**kwargs):

		print("我是A函数")
		
		return func(*args,**kwargs)

	return lala
def c(func):
	def la(*args,**kwargs):
		print("我是C函数")
		return func(*args,**kwargs)

	return la
@a
@c
def b(aa,bb,cc,dd):
	return("b函数计算结果是:%s"%(aa+bb+cc+dd))

print(b(24,9,78,45))

print("****************************************************************")

def a(kk):
	def b():
		print("我是说说")
		kk()
	return b
@a
def c():
	print("dfh")
c()

def a(kk):
	def b():
		print("我是说说")
		ret = kk()
		return ret
	return b
@a
def c():
	return("dfh")
print(c())

print("****************************")

class Test(object):

	def __init__(self, arg):
		print(arg.__name__)
		self.__arg = arg
	def __call__(self):
		print("装饰器中的功能")
		self.__arg
@Test
def a():
	print("WOW")

print(a)
a()
print("********************************************")

#装饰器带参数
def  a(pre="Hello"):
	def b(func):
		def c():
			print(func.__name__)
			return func()
		return c
	return b
@a("wangcai")
def foo():
	print("I am foo")
@a("Python")
def fo():
	print("I am foo")
foo()
fo()
#结果
foo
I am foo
fo
I am foo
print("************************************************")
def upper_attr(future_class_name, future_class_parents, future_class_attr):

    #遍历属性字典，把不是__开头的属性名字变为大写
    newAttr = {}
    for name,value in future_class_attr.items():
        if not name.startswith("__"):
            newAttr[name.upper()] = value

    #调用type来创建一个类
    return type(future_class_name, future_class_parents, newAttr)

class Foo(object, metaclass=upper_attr):
    bar = 'bip'

print(hasattr(Foo, 'bar'))
print(hasattr(Foo, 'BAR'))

f = Foo()
print(f.BAR)