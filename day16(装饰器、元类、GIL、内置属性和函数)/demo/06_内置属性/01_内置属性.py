'''
	__getattribute__魔法方法

	当调用属性的时候自动调用
'''


class Test(object):
	def __init__(self,subject1):
		self.subject1 = subject1
		self.subject2 = 'cpp'
		self.__num=100

	def show(self):
		print('this is Test')

	def __getattribute__(self,attrName):
		if attrName.startswith('__'):
			print('私有属性不能访问')
			raise Exception('%s 是私有的，你没有访问的权限'%attrName)
		else:   #测试时注释掉这2行，将找不到subject2
			return object.__getattribute__(self,attrName)


s = Test("python")
print(s.subject1)
print(s.subject2)

s.show()

#print(s.__num)


print('******************************华丽的分割线******************************')

class Person(object):
	def __getattribute__(self,obj):
		print("---test---")
		if obj.startswith("a"):
			return "hahha"
		else:
			return self.test


	def test(self):
		print("heihei")


t = Person()
print(t.abc)
#t.bbb
