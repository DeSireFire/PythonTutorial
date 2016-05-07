'''
__str__(self):
	return 字符串

当对象转字符串的时候自动调用

'''


class Dog:
	def __init__(self,name,color):
		print('__init__')
		self.name = name
		self.color = color

	def __str__(self):
		print('__str__')
		info = 'name=%s,color=%s'%(self.name,self.color)
		return info


wangcai = Dog('旺财','白')
xiaoqiang = Dog('小强','黑')

#str(wangcai)
print(wangcai)
print(xiaoqiang)