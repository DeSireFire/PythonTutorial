'''

将共性的内容放在父类中，子类只需要关注自己特有的内容。这就是继承。
继承具有传递性。
'''



'''
	宠物系统
'''

class Dog:
	def __init__(self,name,brand,color,sex):
		pass
	def jiao(self):
		pass
	def wanfeipan(self):
		pass


class Cat:
	def __init__(self,name,brand,color,sex):
		pass
	def jiao(self):
		pass
	def wanmaoxian(self):
		pass



'''
父类中定义共性的属性和方法
'''
class Animal(object):
	def __init__(self,name,brand,color,sex):
		self.name = name
	def jiao(self):
		print('jiao...')

'''
子类中定义自己特有的属性和方法
'''
class Dog(Animal):
	def wanfeipan(self):
		print('wanfeipan...')

class Cat(Animal):
	def wanmaoxian(self):
		pass


dog = Dog('旺财','贵宾','白','雄性')
dog.wanfeipan()
dog.jiao()
print(dog.name)