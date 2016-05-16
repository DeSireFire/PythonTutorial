'''
	类属性：
		1、定义在类内部，方法外部的属性就是类属性
		2、在类的外部，通过类对象.属性就是类属性

	

	类属性是属于类对象的，还属于所有实例对象
	

'''
class Dog:
	name = '子庆'
	color = '黑色'
	num=123456
	def run(self):
		print('run...')



'''
d1 = Dog()
d1.name = '旺财'
print(d1.name)

print(dir(Dog))
print(Dog.name)

Dog.sex = '雄'
print(Dog.sex)
print(dir(Dog))
print(d1.sex)
'''


d1 = Dog()
d2 = Dog()
print(d1.name)
print(d2.name)
Dog.name = '旺财'
print(d1.name)
print(d2.name)





'''
d1 = Dog()
d2 = Dog()
print(d1.name)
print(d2.name)
#此时name是一个实例属性
d1.name = '旺财'
print(d1.name)
print(d2.name)
'''

'''
d1 = Dog()
print(id(Dog.name))
print(id(d1.name))

print(Dog.run)
print(d1.run)
print(d2.run)
'''



'''
d1 = Dog()
d2 = Dog()

def stop(self):
	print('stop...')

Dog.stop = stop
print(Dog.stop)

d1.stop()

print(id(d1.stop))
print(id(d2.stop))
print(id(Dog.stop))
'''


'''
d1 = Dog()
d2 = Dog()

def stop(self):
	print('stop...')

Dog.run = stop

d1.run()
'''

