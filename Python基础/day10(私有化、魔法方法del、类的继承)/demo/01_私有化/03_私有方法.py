'''
	私有化的方法

'''


class Dog:
	def __wangwang(self):
		print('汪汪.....')

	def haha(self):
		print('haha.....')
		#前面加业务逻辑
		self.__wangwang()
		#后面加业务逻辑

	def f1(self):
		print('f1...')
		self.f2(120)

	def f2(self,num):
		print('f2...%s'%num)


wangcai = Dog()
#wangcai.__wangwang()
wangcai.haha()

wangcai.f1()
