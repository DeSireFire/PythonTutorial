class Beauty:
	def __init__(self,name,weight):
		self.name = name
		self.weight = weight
	
	def getAge(self):
		return self.__age

	def setAge(self,age):
		if 0<age<120:
			self.__age = age
		else:
			self.__age = 18
			print('年龄不符合要求，默认18')



caofan = Beauty('曹反',80)

#print(caofan.getAge())

caofan.setAge(18888)

print(caofan.getAge())



'''
对于访问的属性或者方法
	1、公共的
	2、私有的


有些属性是不能直接对外访问的，所以设置成私有化

如果对外访问，需要提供可以访问的方法，然后可以在在这样的方法中，设置一些业务逻辑。

'''




class Beauty:
	def __init__(self,name,weight):
		self.name = name
		self.weight = weight
		self.__age = 18
	
	def getAge(self):
		return self.__age

	def setAge(self,age):
		if 0<age<120:
			self.__age = age
		else:
			print('年龄不符合要求，默认18')



caofan = Beauty('曹反',80)

print(caofan.getAge())

caofan.setAge(20)

print(caofan.getAge())