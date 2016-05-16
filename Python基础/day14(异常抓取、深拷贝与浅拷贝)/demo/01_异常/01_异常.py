'''
异常：
	1、程序运行报错
	2、逻辑混乱

一旦出现异常：程序报错，停止


如果出现异常：
	给用户提示
否则：
	继续运行
'''

open('xx.txt','r')

def add(*num):
	return sum(num)

print(add(1,2))
print(add(1,'2'))



