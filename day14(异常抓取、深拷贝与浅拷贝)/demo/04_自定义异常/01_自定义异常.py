'''
以后在项目中，会对各种异常进行统一管理。

try:
	...
except Exception as ex:
	记录日志文件中
	给客户提示
	...


'''

'''

def info():
	sex = input('请输入性别：')
	if sex!='男' or sex!='女':
		
	else:
		print(sex)

try:
	info()
except Exception as ex:
	#记录日志文件中
	#给客户提示
	#...
'''


'''
怎么自定义异常：

	class MyException(Exception):
		pass


	此时MyException就是一个自定义异常类

'''
class SexException(Exception):
	def __init__(self,msg):
		self.msg = msg
	

def info():
	"""获取性别。如果性别输入不是男或者女，抛出一个SexException的异常"""
	sex = input('请输入性别：')
	if sex!='男' and sex!='女':
		raise SexException('性别只能是男或者女')
	return sex


def main():
	try:
		print(info())
		#。。。。
	except Exception as ex:
		print('异常信息是:%s'%ex.msg)

	#info()

main()


'''
Exception

	def __str__(self):
		return 找到self的实例属性组成的元组
'''




class ShortInputException(Exception):
	'''自定义的异常类'''
	def __init__(self, length, atleast):
		#super().__init__()
		self.length = length
		self.atleast = atleast

def main():
	try:
		s = input('请输入 --> ')
		if len(s) < 3:
			# raise引发一个你定义的异常
			raise ShortInputException(len(s), 3)
	except ShortInputException as result:#x这个变量被绑定到了错误的实例
		print('ShortInputException: 输入的长度是 %d,长度至少应是 %d'% (result.length, result.atleast))
	else:
		print('没有异常发生.')

main()
