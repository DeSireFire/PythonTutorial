'''
	python支持多继承。
	一个类可以有多个父类
'''

class Donkey:
	def f1(self):
		print('Donkey。。。')


class Horse:
	def f2(self):
		print('Horse。。。')



class Mule(Donkey,Horse):
	def f3(self):
		print('Mule。。。')


	

mule = Mule()
print(dir(mule))
mule.f1()
mule.f2()
mule.f3()

'''
基类(父类)
派生类(子类)
'''
print(Mule.__bases__)
print(Mule.__mro__)

