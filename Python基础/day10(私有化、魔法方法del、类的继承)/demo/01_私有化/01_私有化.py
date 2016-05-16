'''
在python中，前缀是__的都是私有的

__age						私有的属性



def __haha(self):			私有的方法
	pass



这两个都是私有的



有的属性，不能对外访问。应该设置成私有化的属性。

私有化之后，在类外不能访问。
如果还想访问和设置，但是有所控制。

外：类外
'''
class Beauty:
	def __init__(self,name,age,weight):
		self.name = name
		self.__age = age
		self.weight = weight


		




caofan = Beauty('曹反',18,80)
#print(caofan.age)
#print(caofan.__age)



'''

私有化的属性，对内可以访问

内：类的内部
'''

class Beauty:
	def __init__(self,name,age,weight):
		self.name = name
		self.__age = age
		self.weight = weight
	
	def getAge(self):
		return self.__age



caofan = Beauty('曹反',18,80)
age = caofan.getAge()
print(age)





