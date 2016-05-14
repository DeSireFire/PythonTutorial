from time import ctime

'''
传递参数，用于后面的业务逻辑
参数值的不同，业务逻辑可能不同
'''


'''
def outer(num):
	print('1...')
	def timefun(func):
		print('2...')
		def wrappedfunc():
			print("%s called at %s %s"%(func.__name__, ctime(), num))
			return func()
		return wrappedfunc
	return timefun





@outer(100)
def too():
	print("I am too")

too()
'''

def wrapper(num):
	def outer(func):
		def inner():
			if num%2==0:
				print('权限的验证')	
			else:
				print('日志的记录')
			return func()
		return inner
	return outer

@wrapper(2)
def too():
	print("I am too")

too()

