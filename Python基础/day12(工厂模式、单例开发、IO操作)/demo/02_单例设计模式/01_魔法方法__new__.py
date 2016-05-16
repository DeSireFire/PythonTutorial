'''
	魔法方法__new__功能：
		1、创建对象
		2、返回创建的对象



	class object:
		def __new__(*args, **kwargs):
			1、创建对象
			2、返回对象
   
	
'''


class A:
	def __init__(self):
		print('__init__...')

	def __new__(cls):
		print('__new__...')
		#obj =  object.__new__(cls)
		obj =  super().__new__(cls)
		return obj
		
	

'''
	1、调用__new__，返回了一个实例对象
	2、调用__init__,将1返回的实例对象，作为参数给self
'''
A()






class B:
	def __init__(self,name,age,num):
		print('__init__...')
		self.name = name
		self.age = age
		self.num = num	

	'''
	def __new__(cls,*args,**kwargs):
		print('__new__...')
		print(args)
		print(kwargs)
		obj =  object.__new__(cls)
		return obj
	'''
	def __new__(*args,**kwargs):
		print('__new__...')
		obj =  object.__new__(args[0])
		return obj

		
	

'''
	1、自动调用__new__，返回了一个实例对象
	2、自动调用__init__,将1返回的实例对象，作为参数给self
			如果在__init__有参数，也会自动为__init__的其它参数赋值
'''
b = B('老王',10,110)
print(b.name)

