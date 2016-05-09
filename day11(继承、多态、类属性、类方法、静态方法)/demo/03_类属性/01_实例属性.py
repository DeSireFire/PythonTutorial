'''
	实例属性：
		1、在类中，self.属性    self当前实例对象
		2、在类外，实例对象.属性

		实例对象.属性

'''

class Dog:
	def __init__(self,name,color):
		self.name = name
		self.color = color

	def f(self,num):
		self.num = num

	

d = Dog('子庆','黑色')
print(dir(d))

d.sex = '雄'

print(dir(d))

d.f(110)

print(dir(d))
