def choose_class(name):
	if name == 'foo':
		class Foo(object):
			pass
		return Foo     # 返回的是类，不是类的实例
	else:
		class Bar(object):
			pass
		return Bar


ret = choose_class('foo')
print(ret)

print('***************************************华丽的分割线***************************************')



'''
	使用type创建类
	

	type的第3个参数
	1、字符串 类名
	2、元组   父类
	3、字典	  类属性
'''


'''
class Test:
	pass
'''
Test = type('Test',(),{})
print(Test)


Test = type('Test',(),{'name':'老王','age':10})

print(Test.name)


class Fu:
	def fu(self):
		print('fu...')

Zi = type('Zi',(Fu,),{})
print(Zi.__mro__)


print('***************************************华丽的分割线***************************************')

def haha(self):
	print('haha...')

def __init__(self,num):
	print('self...')
	self.num = num

@classmethod
def hehe(cls):
	print('hehe...')

Test = type('Test',(),{'name':'老王','age':10,'haha':haha,'hehe':hehe,'__init__':__init__})

t = Test(110)
t.haha()

Test.hehe()

print('***************************************华丽的分割线***************************************')

def upper_attr(future_class_name, future_class_parents, future_class_attr):

	print(future_class_name)
	print(future_class_parents)
	print(future_class_attr)

	#遍历属性字典，把不是__开头的属性名字变为大写
	newAttr = {}
	for name,value in future_class_attr.items():
		if not name.startswith("__"):
			newAttr[name.upper()] = value

	#调用type来创建一个类
	return type(future_class_name, future_class_parents, newAttr)


'''
	metaclass=upper_attr
	表示次类创建的时候，按照upper_attr的约束创建类

	自动的调用upper_attr函数，将Foo的类名，父类，属性都传递过去。
	执行完函数，得到一个返回值，是一个类对象 xx
	Foo = xx

'''
class Fu:
	pass

class Foo(Fu, metaclass=upper_attr):
	bar = 'bip'

print(hasattr(Foo, 'bar'))
print(hasattr(Foo, 'BAR'))
print(dir(Foo))

print(Foo.BAR)

print('***************************************华丽的分割线***************************************')

class UpperAttrMetaClass(type):
   
	def __new__(cls, future_class_name, future_class_parents, future_class_attr):
		print('1...')
		newAttr = {}
		for name,value in future_class_attr.items():
			if not name.startswith("__"):
				newAttr[name.upper()] = value
		return super().__new__(cls, future_class_name, future_class_parents, newAttr)
		
class Foo(object, metaclass = UpperAttrMetaClass):
	bar = 'bip'


print(Foo.BAR)


