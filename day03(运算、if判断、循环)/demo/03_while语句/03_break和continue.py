'''
1-100的和
'''

'''
num = 1
ret = 0
while num<101:
	ret+=num
	num+=1
print(ret)
'''

'''
num = 1
ret = 0
while True:
	ret+=num
	num+=1
	if num>100:
		break
print(ret)
'''

'''
num = 1
year = 2017
rate = 0.0035
while True:
	year+=1
	num = num*(1+rate)
	if num>=2:
		break
print(year)
'''

num = 0
while num<100:
	num+=1
	if num%3==0:
		continue
	print(num)
	



'''
break是跳出自己所在最近的循环

continu是结束当前这一次循环，进入下一次循环
'''