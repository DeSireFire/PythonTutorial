'''
	对象也是可变类型

	函数是不可变类型
'''

class Dog:
	pass


d1 = Dog()
d2 = d1

d1.name = '旺财'
print(d2.name)






def f(dog):
	dog.color = '黑色'

d1 = Dog()
f(d1)		#dog=d1  实例对象的传递
print(d1.color)
