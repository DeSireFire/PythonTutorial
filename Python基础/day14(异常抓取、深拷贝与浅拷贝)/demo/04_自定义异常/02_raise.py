'''
raise  抛出任何异常（自定义的，系统自带的）。


1、raise 异常对象
2、raise 配合except使用

一般在框架中异常的处理：
	1、将异常信息写到文件中，日志文件
	2、继续抛出异常
'''


def test1():
	print("----test1-1----")
	print(num)
	print("----test1-2----")




def test3():
	try:
		print("----test3-1----")
		test1()
		print("----test3-2----")
	except Exception as result:
		print("捕获到了异常，信息是:%s"%result)
		#raise result
		raise
		

	print("----test3-2----")



try:
	test3()
except Exception as ex:
	#1、将异常信息写到文件中，日志文件
	#2、其它处理。不如将网页跳转到显示错误信息的页面（404  500   网页找不到，网站正在维护中。。。）
	print('记录日志：%s'%ex)