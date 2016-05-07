'''
class k(object):
	def __init__(self,kaotime=0,kaorange='生',cooik=[]):
		self.kaotime = kaotime
		self.kaorange = kaorange
		self.cooik = cooik

	def __str__(self):
		info = ".".join(self.cooik)
		msg = '时间:%s,成度:%s,调料:%s'%(self.kaotime\
			,self.kaorange,info)
		return msg

	def kao(self,times):
		self.kaotime += times
		if(self.kaotime<=3):
			self.kaorange = '生'
		elif(self.kaotime<=5):
			self.kaorange = '半熟'		
		elif(self.kaotime<=8):
			self.kaorange = '熟啦，烤的正好'
		else:
			self.kaorange = '坏事，烤成木炭了'

	def cc(self,n):
		self.cooik.append(n)

kk1 = k()
kk1.kao(4)
#print(kk1.kaorange)
kk1.cc('番茄酱')
kk1.cc('沙拉')
kk1.cc('孜然')

print(kk1)
'''

'''
#烤牛排

class niupai(object):
	def __init__(self,times=0,level='生的',flavour=['三鲜']):
		self.times = times
		self.level = level
		self.flavour = flavour
	def shu(self,timess):
		self.times += timess
		if self.times<=10:
			self.level = '别急客官，还没有好'
		elif self.times <=20:
			self.level = '稍等客官，马上就好'
		elif self.times <= 30:
			self.level = '麻烦客官让一下，您的牛排好了'
		else:
			self.level = '不好意思客官，厨师是个新来的，您要的牛排考坏了，稍等我再给你烤一份'
	def flavours(self,ms):
		self.flavour.append(ms)
	def __str__(self):
		info = '.'.join(self.flavour)
		info1 = str(self.flavour)
		info2 = info1[1:len(info1)-1]
		msg = '牛排烤的时间是:%s分钟,%s,牛排味道是:%s'%(self.times,self.level,info)
		return msg
xiaowang = niupai()
xiaowang.shu(25)
xiaowang.flavours('孜然味')
xiaowang.flavours('麻辣味')
print(xiaowang)
'''
'''
#房间空间大小
class home:
	def __init__(self,area):
		self.area = area
		#房间其他家具
		self.contains = []
	def __str__(self):
		msg = '当前房间总面积是:'+str(self.area)
		if len(self.contains)>0:
			msg = msg + '容纳物品有:'
			for m in self.contains:
				msg = msg + m.getname() + ','
			msg = msg.strip(',')
		return msg
	#容纳物品
	def accommodate(self,item1):
		needarea = item1.getusedarea()
		if self.area > needarea:
			self.contains.append(item1)
			self.area -= needarea
			print('好了，已经存放在房间中了!!!')
		else:
			print('物品过大%s，空间剩余%已经存放不下了!!!'%(needarea,self.area))

class bed:
	def __init__(self,area,name='床'):
		self.area = area
		self.name = name

	def __str__(self):
		msg = '床的面积是:' + str(self.area)
		return msg
	#获取床的面积
	def getusedarea(self):
		return self.area
	def getname(self):
		return self.name

#创建对象
home1 = home(120)
print(home1)
#创建床对象

bed = bed(20)
print(bed)
#把床放到家中
home1.accommodate(bed)
print(home1)


#创建一个床对象
bed1 = bed(30,'桌')
print(bed1)
#把床放到家中
home1.accommodate(bed1)
print(home1)

'''
#存放家具
class home:
	def __init__(self,area,jiajus=[]):
		self.area = area
		self.jiajus = jiajus
	
	def __str__(self):
		msg=''
		num = self.area
		for n in self.jiajus:
			num += n.daxiao
			msg += str(n)
			msg += ' | '
		msg = msg.rstrip(' | ')
		
		return '总面积：%s,剩余面积:%s,%s'%(num,self.area,msg)

	def cunjiaju(self,jiaju):
		if self.area > jiaju.daxiao:
			self.jiajus.append(jiaju)
			self.area -= jiaju.daxiao
		else:
			print('家具太大，放不下!!!')

class jaj:
	def __init__(self,daxiao,name):
		self.name = name
		self.daxiao = daxiao
	def __str__(self):
		msg1 = '家具是:%s,大小是:%s'%(self.name,self.daxiao)
		return msg1


xiaohong = home(120)

jia = jaj(10,'床')
xiaohong.cunjiaju(jia)

jia1 = jaj(15,'茶几')
xiaohong.cunjiaju(jia1)

print(xiaohong)