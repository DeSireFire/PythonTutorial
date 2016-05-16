'''
	设计：在简单工厂模式的基础上。每一类对象都有对应的一个工厂。

	一般会有对应的配置文件，将具体角色与工厂一一对应起来
		Haval---HavalFactory
		Geery--GeeryFactory
		Changan--ChanganFactory
'''



#抽象产品角色
class Car:
	def move(self):
		pass

#具体产品角色
class Haval(Car):
	def move(self):
		print("---haval 车在移动---")

#具体产品角色
class Geery(Car):
	def move(self):
		print("---Geery 车在移动---")

#具体产品角色
class Changan(Car):
	def move(self):
		print("---Changan 车在移动---")
	


#抽象工厂角色
class Factory:
	@classmethod
	def createCar(cls):
		pass

#具体工厂角色
class HavalFactory:
	@classmethod
	def createCar(cls,name):
		ret = None
		if name == '哈弗':
			return Haval()

#具体工厂角色
class GeeryFactory:
	@classmethod
	def createCar(cls,name):
		ret = None
		if name =='吉利':
			return Geery()

#具体工厂角色
class ChanganFactory:
	@classmethod
	def createCar(cls,name):
		ret = None
		if name == '长安':
			return Changan()


def main():
	car = HavalFactory.createCar('哈弗')
	if car!=None:
		car.move()
	print(car)


main()


