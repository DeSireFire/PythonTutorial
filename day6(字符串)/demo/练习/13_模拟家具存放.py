'''
存放家具
'''
'''
class home:
	def __init__(self,daxiao,jiajus=None):
		jiajus=[]
		self.daxiao = daxiao
		self.jiajus = jiajus
	def __str__(self):
		num = self.daxiao
		for n in self.jiajus:
			num += n.daxiao
		msg = '家庭总面积:%s,家庭剩余总面积:%s'%(num,self.daxiao)

		return msg
	def cunfang(self,jiaju):
		if self.daxiao>jiaju.daxiao:
			self.jiajus.append(jiaju)
			self.daxiao-=jiaju.daxiao
		else:
			print('空间不够，存储不下了!!!')
class jia:
	def __init__(self,name,daxiao):
		self.name = name
		self.daxiao = daxiao
	def __str__(self):
		msg = '家具名字:%s,家具大小:%s'%(self.name,self.daxiao)
		return msg
hh = home(120)
ll = jia('电脑',5)
hh.cunfang(ll)
print(hh)
print(ll)

hh1 = home(110)
ll1 = jia('麻将桌',10)
hh1.cunfang(ll1)
print(hh1)
print(ll1)
'''
