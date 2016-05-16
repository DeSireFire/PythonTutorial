'''
	if:
		条件语句1………………
		条件语句2………………
	else:
		条件语句a
		条件语句b
		………………
	注意：
		1.if  else 后面都需要有冒号
		2.if条件语句中只存在真True或者假False
		3.条件语句要进行缩进
'''

a = int(input('请输分数:'))
if a < 0 or a > 100:
	print('输入出错!!!')
else:
	if a < 60:
		print('不及格')
	elif a <70:
		print('差')
	elif a <80:
		print('中')
	elif a <90:
		print('良')
	else:
		print('优')
print('判断结束!!!')
'''
a = int(input('请输分数:'))
la = 0
i = 1
while i<a:
	i+=1
	la += i
print(la)
'''

'''
num = 1
k = 0
while num < 101:
	k += num
	num+=1
print(k)
'''
'''
a = 1
while a < 20:
	print(a)
	a += 1
	if(a==10):
		break
print('结束')
'''
