'''
父类私有的属性、方法都是不能被继承的
'''

class Father:
	def __init__(self):
		self.__num = 20
	def __haha(self):
		print('haha...')
	def getNum(self):
		return self.__num
	
class Son(Father):
	def getNum2(self):
		return self.__num

son1 = Son()
#print(son1.__num)
#son1.__haha()
'''
num = son1.getNum()
print(num)
'''

'''
num = son1.getNum2()
print(num)
'''
