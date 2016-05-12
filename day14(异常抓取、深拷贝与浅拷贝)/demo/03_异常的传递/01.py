'''
所有的异常，在python都以各种类进行了描述。
代码出现了异常，其实是解析器，找到对应的描述类，创建了一个对应的实例对象，然后抛出。
'''



import time
try:
	#f = open('test.txt')
	f = open(r'C:\Users\Administrator\Desktop\软件\老王.txt','r')
	try:
		while True:
			content = f.readline()
			if leneak(content) == 0: 
				br
			time.sleep(2)
			print(content)
	finally:
		f.close()
		print('关闭文件')

except FileNotFoundError:
	print("没有这个文件")
except UnicodeDecodeError:
	print("编码格式有问题")
