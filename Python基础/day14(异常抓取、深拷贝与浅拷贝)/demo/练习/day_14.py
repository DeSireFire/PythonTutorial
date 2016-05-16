'''
n = int(input("请输入一个数字:"))

try:
	print("开始测试异常是否出现!!!")
	sum = 1
	sum += n
	print("判断是否有异常!!!")
except:
	print("有异常，捕获掉!")
print("继续执行!!!%s"%sum)


try:
	print("开始测试异常是否出现!!!")
	a += n
	print("判断是否有异常!!!")
except NameError as e:
	print("有异常，捕获掉!%s"%e)
print("继续执行!!!%s"%sum)

try:
	print("开始测试异常是否出现!!!")
	#a += n
	m = 2/0
	print("判断是否有异常!!!")
except (NameError,ZeroDivisionError) as e:
	print("有异常，捕获掉!      %s"%e)
print("继续执行!!!%s"%sum)

try:
	print("开始测试异常是否出现!!!")
	sum = 1
	sum += n
	print("判断是否有异常!!!")
except:
	print("有异常，捕获掉!")
else:
	print("没有异常，继续执行!!!")
	print("sum = %s"%sum)
print("执行结束!!!")
'''
file = None
try:
	file = open(r"C:\Users\Administrator\Desktop\07_1.txt")
	sum = 2/1
except Exception as e:
	print("异常是：%s"%e)
else:
	print("啦啦啦，没有异常!!!sum = %s"%sum)
finally:
	print("不管是否有异常，我都执行!!!")
	if file != None:
		file.close()
		print("文件是否关闭状态:%s"%file.closed)
	else:
		print("文件为空None！！！")		
print("执行结束！！！")

#异常的传递
print("*****************************************************")
import time

try:
	file = open(r"C:\Users\Administrator\Desktop\a.txt","r")
	try:
		while True:
			content = file.readline()
			if len(content)==0:
				break
			#time.sleep(0.3)
			print(content)
	finally:
		file.close()
		print("关闭文件")
except:
	print("没有这个文件")

print("*****************************************************")

class wodeexception(Exception):
	def __init__(self,msg):
		self.msg = msg
def lala():
	n = input("请输入一个不多于5位的数字:")
	if len(n)>5:
		raise wodeexception("输入超过系统范围!!!")
	return n
def main():
	try:
		print(lala())
	except Exception as e:

		print("哈哈哈,异常信息是:%s"%e)
main()

print("*****************************************************")

def test1():
	print("----test1-1----")
	print(num)
	print("----test1-2----")


def test2():
	print("----test2-1----")
	test1()
	print("----test2-2----")


def test3():
	try:
		print("----test3-1----")
		test1()
		print("----test3-2----")
	except Exception as result:
		print("捕获到了异常，信息是:%s"%result)

	print("----test3-2----")



test3()
print("*****************************************************")
#test2()
class woexception(Exception):
	def __init__(self,msg,la):
		self.msg = msg
		self.la = la
def lalaa():
	try:
		n = input("请输入一个不多于5位的数字:")
		if len(n)<5:
			raise woexception(len(n),5)
	except Exception as e:
		print("您输入的长度是:%s，应该输入的长度是:%s"%(e.msg,e.la))
	else:
		print("没有发生异常!!!")
lalaa()
#raise 抛出任何异常信息

print("*****************************************************")

def test1():
	print("test1-1*************")
	print(num)
	print("test1-2*************")
def test2():
	try:
		print("test2-1*************")
		test1()
		print("test2-2*************")
	except Exception as e:
		print("捕获到了异常信息:%s"%e)
		raise
	print("test2-3*************")
try:
	test2()
except Exception as e:
	print("记录日志:%s"%e)

