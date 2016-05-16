'''
	属性：
		1、cookedLevel				烤地瓜时间
		2、cookedDescription		地瓜状态的描述
		3、condiments				调料


	方法：
		1、cook(time)				烤地瓜
		2、addCondiment(con)		加调料

'''
class RoastedSweetPotato:
	'''这是烤地瓜的类'''
	def __init__(self,cookedLevel=0,cookedDescription='生',condiments=[]):
		'''初始化属性'''
		self.cookedLevel = cookedLevel
		self.cookedDescription = cookedDescription
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
	


	
'''		
rsp1 = RoastedSweetPotato()
print(rsp1.cookedLevel)
rsp1.cook(1)
rsp1.cook(4)
rsp1.cook(2)
print(rsp1.cookedDescription)
rsp1.cook(30000000000000)
print(rsp1.cookedLevel)
print(rsp1.cookedDescription)


rsp1.addCondiment('芥末')
rsp1.addCondiment('番茄酱')
rsp1.addCondiment('黄豆酱')
print(rsp1.condiments)


rsp2 = RoastedSweetPotato()
print(rsp2.cookedLevel)


print(rsp1)
print(rsp2)

print(str(rsp1))
print(str(rsp2))
'''
'''
rsp1 = RoastedSweetPotato()
rsp2 = RoastedSweetPotato()
'''


'''
class roasted_sweet_potato:
	pass
'''


rsp1 = RoastedSweetPotato()
rsp1.addCondiment('芥末')
print(rsp1)


rsp2 = RoastedSweetPotato()
rsp2.addCondiment('黄豆酱')
print(rsp2)