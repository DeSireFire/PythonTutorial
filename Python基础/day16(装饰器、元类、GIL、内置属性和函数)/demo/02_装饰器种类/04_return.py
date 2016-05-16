'''

为了提高通用性，所有的装饰器中，return
'''


from time import ctime, sleep

def timefun(func):
	def wrappedfunc():
		print('begin...')
		ret = func()
		print('end...')
		return ret
	return wrappedfunc

@timefun
def foo():
	print("I am foo")

@timefun
def getInfo():
	return '----hahah---'




print(getInfo())

foo()
