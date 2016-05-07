
def f(num,ls=[]):
	ls.append(num)
	return ls

'''
print(f(110))
print(f(120))
'''

ret1 = f(110)
print(ret1)

#ret1.append(919)

ret2 = f(120)
print(ret2)





def f(num,ls=None):
	if ls==None:
		ls = []
	ls.append(num)
	return ls


print(f(110))
print(f(120))


print(f(119,[10,20]))
print(f(250,[10,20]))





class RoastedSweetPotato:
	'''这是烤地瓜的类'''
	def __init__(self,cookedLevel=0,cookedDescription='生',condiments=None):
		'''初始化属性'''
		self.cookedLevel = cookedLevel
		self.cookedDescription = cookedDescription
		if condiments==None:
			condiments=[]
		self.condiments = condiments

	def __str__(self):
		'''转成字符串'''
		info1 = str(self.condiments)
		info2 = 'cookedLevel=%s,cookedDescription=%s,condiments=%s'%(self.cookedLevel,self.cookedDescription,info1[1:len(info1)-1])
		return info2

	def cook(self,time):
		'''
			烤地瓜，随着时间的增加，cookedLevel，cookedDescription改变
			time：烤地瓜的分钟数
		'''
		self.cookedLevel += time
		if self.cookedLevel <=3:
			self.cookedDescription = '生'
		elif self.cookedLevel<=5:
			self.cookedDescription = '半熟'
		elif self.cookedLevel<=8:
			self.cookedDescription = '熟'
		else:
			self.cookedDescription = '木炭'

	def addCondiment(self,con):
		'''
			增加调料
		'''
		self.condiments.append(con)




rsp1 = RoastedSweetPotato()
rsp1.addCondiment('芥末')
print(rsp1)


rsp2 = RoastedSweetPotato()
rsp2.addCondiment('黄豆酱')
print(rsp2)



rsp3 = RoastedSweetPotato(condiments=['辣椒','大蒜'])
rsp3.addCondiment('黄豆酱')
print(rsp3)