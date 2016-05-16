'''
	房子

	属性：
		1、面积				int
		2、家具				list

	方法：
		1、存放家具：参数  家具对象


	家具：
		属性：
			1、面积
'''


class House:
	
	def __init__(self,area=100,furnitures=[]):
		self.area = area
		self.furnitures = furnitures
	
	def storeFurniture(self,furniture):
		if self.area>furniture.area:
			self.furnitures.append(furniture)
			self.area -= furniture.area

	def __str__(self):
		msg=''
		num = self.area
		for i in self.furnitures:
			num+=i.area
			msg+=str(i)
			msg+='|'
		msg = msg.rstrip('|')
		return '总面积=%s,剩余面积=%s,家具=%s'%(num,self.area,msg)


class Furniture:
	def __init__(self,area,name):
		self.area = area
		self.name = name

	def __str__(self):
		return 'area=%s,name=%s'%(self.area,self.name)



house = House(200)

bed = Furniture(5,'大床')
house.storeFurniture(bed)

desk = Furniture(4,'桌子')
house.storeFurniture(desk)

print(house)
print(bed)