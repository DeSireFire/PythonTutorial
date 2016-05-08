'''
#属性私有化
class D(object):
	def __init__(self,name,address):
		self.name = name
		self.address = address
	def __str__(self):
		msg = '年龄:%s 地址:%s'%(self.name,self.address)
		return msg
	def get_age(self):
		return self.__age

	def set_age(self,age):
		if 0 < age <110:
			self.__age = age
		else:
			print('不符合常规!!!')
xiao = D('小红','郑州')
xiao.set_age(18)
print(xiao,end='')
print(' 年龄:%s'%xiao.get_age())

#方法私有化
class D(object):

	def shangban(self):
		print('要去上班!!!')
		self.__fangshi('骑车')
		self.dizhi()
	def __fangshi(self,a):
		print('上班方式:%s'%a)
	def dizhi(self):
		print('地址:郑州')
	
xiao = D()
xiao.shangban()

#属性私有化
class la():

	def __init__(self,name,tel,address):
		self.name = name
		self.tel = tel
		self.address = address

	def get_age(self):
		return self.__age

	def set_age(self,age):
		if(16<age<30):
			self.__age = age
			#print('找这个年龄段的人!!!')
		else:
			print('不要不在这个年龄段的人!!!')

	def get_weight(self):
		return self.__weight

	def set_weight(self,weight):
		if(40<weight<60):
			self.__weight = weight
			#print('找这个体重段的人!!!')
		else:
			print('不要不在这个体重段的人!!!')

	def __str__(self):
		msg = '年龄:%s 电话:%s 地址:%s 年龄:%s 体重:%s'%(self.name,\
			self.tel,self.address,self.get_age(),self.get_weight())
		return msg

zhao = la('小红',120,'郑州')
zhao.set_age(20)
zhao.set_weight(50)

print(zhao)
print('******************************************************')

class l:

	def __del__(self):
		print('我是del删除对象时候用到的!!!')

	def la(self,name):
		print('我的名字是:%s'%name)
wo = l()
ni = wo
wo.la('小红')
import sys
print('$$$$$$$$$$$$$$$$$$$$$$$$')
#del ni
m = sys.getrefcount(wo)-1
print(m)
'''

'''
继承
'''
class animal(object):
	def __init__(self,name,range,color):
		self.name = name
		self.range = range
		self.color = color

	def eat(self,food):
		print('我正在吃:%s'%food)

	def sleep(self):
		print('我困了，我要睡觉!!!')

	def __str__(self):
		msg = 'name:%s range:%s color:%s'%(self.name,self.range,self.color)
		return msg

class dog(animal):

	def han(self,jiao):
		print('%s……………………………'%jiao)
class cat(animal):

	def pashu(self):
		print('我正在爬树！！！')
#多次继承
class o(dog):
	def __init__(self,names,tt):
		self.names = names
		self.tt = tt
	def la(self):
		print('啦啦啦，我粑粑是李刚!!!')
		print(self.names,self.tt)

print('********************************************')
d = dog('旺财','啸天犬','黑色')
d.han('汪汪')
d.eat('热狗')
print(d)
print('********************************************')
m = cat('小猫','加菲','白色')
m.pashu()
m.sleep()
print(m)
print('********************************************')
kk = o('富三代','土豪金')
kk.han('lal')

#多继承
class ma(object):
	def l(self):
		print("我是马!!!")
class lv(object):
	def l1(self):
		print("我是驴!!!")

class luo(ma,lv):
	def l2(self):
		print("我是骡!!!")
k = luo()
k.l()
k.l1()
k.l2()
print(luo.__bases__)
print(luo.__mro__)
print()
print('&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&')
print()
#重写
class D:
	def s(self):
		print('11111111111111111111111111111111')
class F(D):
	def s(self):
		print('22222222222222222222222222222222')
c = F()
c.s()
print()
print('&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&')
print()

#调用父类方法

class fu:
	def __init__(self,name):
		self.name = name
		self.range = '一级甲等'
class zi(fu):
	def __init__(self,name):
		super().__init__(name)
	def getname(self):
		return self.name
bb = zi('我是子类!!!')
print(bb.name)
print(bb.range)