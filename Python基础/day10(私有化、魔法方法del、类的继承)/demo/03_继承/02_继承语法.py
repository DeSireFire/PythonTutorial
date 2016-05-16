'''
	class 父类(object):
		pass

	class 子类(父类):
		pass


	父类私有的内容不能被继承。
'''

class Cat:
	def __init__(self,name,color):
		print('__init__...%s...%s'%(self,type(self)))
		self.name = name
		self.color = color
	def run(self):
		print('名字叫%s,颜色是%s的猫run...'%(self.name,self.color))


class Garfield(Cat):
	def stop(self):
		print('名字叫%s,颜色是%s的猫stop...'%(self.name,self.color))



g1 = Garfield('加菲','棕色')
print(g1)
print(type(g1))
#g1.run()
g1.stop()


c1 = Cat('加菲','棕色')
