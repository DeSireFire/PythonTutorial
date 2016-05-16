'''
	循环：
		1、循环的条件
			如果循环条件为真，循环执行
		2、循环体
'''
num = 0
while num<10:
	num+=1
	print('爱你一万年。。。。。。%s'%num)
	

print('over......')


num = 1
while num<11:
	print('爱你一万年。。。。。。%s'%num)
	num+=1
	

print('over......')


'''
	打印从1-100时间的偶数
'''

num = 1
while num<101:
	if num%2==0:
		print(num)
	num+=1

num = 2
while num<101:
	print(num)
	num+=2
