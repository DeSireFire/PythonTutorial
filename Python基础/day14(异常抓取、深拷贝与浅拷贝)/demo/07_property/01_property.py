class Person(object):
	def __init__(self):
		self.__money = 0

	def getMoney(self):
		return self.__money

	def setMoney(self, value):
		if isinstance(value, int):
			self.__money = value
		else:
			print("error:不是整型数字")


laowang = Person()
print(laowang.getMoney())
laowang.setMoney(10000000)
print(laowang.getMoney())

print('********************************华丽的分割线********************************')




class Person(object):
	def __init__(self):
		self.__money = 0

	def getMoney(self):
		return self.__money

	def setMoney(self, value):
		if isinstance(value, int):
			self.__money = value
		else:
			print("error:不是整型数字")
	'''
		当获取money属性，调用getMoney方法
		当设置money属性，调用setMoney方法
	'''
	money = property(getMoney,setMoney)


laowang = Person()
print(laowang.money)
laowang.money = 1000000
print(laowang.money)


print('********************************华丽的分割线********************************')




class Person(object):
	def __init__(self):
		self.__money = 0

	@property
	def money(self):
		return self.__money

	@money.setter
	def money(self, value):
		if isinstance(value, int):
			self.__money = value
		else:
			print("error:不是整型数字")
	

laowang = Person()
print(laowang.money)

laowang.money = 100000


print(laowang.money)

