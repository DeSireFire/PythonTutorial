'''
	买车
	面向对象：
		类：
			1、各种车类
			2、4s
			3、工厂
			4、客户

	

	简单工厂设计模式：
		1、工厂类角色
		2、抽象产品角色（父类）
		3、具体产品角色（子类）
	
'''
class Haval:
	def move(self):
		print("---车在移动---")
	def stop(self):
		print("---停车---")


class H9(Haval):
	def move(self):
		print("---车在移动---")
	def stop(self):
		print("---停车---")


class H8(Haval):
	pass

	
class H7(Haval):
	pass

class H6(Haval):
	pass



class Factory:
	@classmethod
	def createCar(cls,name):
		ret = None
		if name=='h9':
			ret = H9()
		elif name=='h8':
			ret = H8()
		elif name=='h7':
			ret = H7()
		elif name=='h6':
			ret = H6()
		return ret

'''
函数式编程，一般不用，建议使用面向对象的方式创建类
def createCar(name):
	ret = None
	if name=='h9':
		ret = H9()
	elif name=='h8':
		ret = H8()
	return ret



def main():
	car = createCar('h9')
	car.move()
	car.stop()

'''
def main():
	car = Factory.createCar('h8')
	car.move()
	car.stop()

	car = Factory.createCar('h9')
	car.move()
	car.stop()

main()

	


'''

#抽象角色，一般是只定义功能，没有实现。还可以定义功能，根据需要，是否重写
class Haval:
	def move(self):
		pass
	def stop(self):
		pass


class H9(Haval):
	def move(self):
		print("h9 ---车在移动---")
	def stop(self):
		print("h9 ---停车---")

'''