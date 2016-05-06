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

'''
read = int(input('请输入你的查询序号:'))
print('你输入的查询符号为:%d'%(read))
if read >=100:
	print('你需要交5%的个人所得税!!!')
elif 50<read<100:
	print('你需要交2%的个人所得税!!!')
else:
	print('你不需要交税，哈哈!!!')
print('判断语句结束。。。。')
'''

'''
read = int(input('请输入年份:'))
if ((read%4==0) and (read%100!=0)) or (read%400==0):
	print('%d是闰年'%(read))
else:
	print('%d不是闰年'%(read))
print('判断结束')
'''

'''
a = int(input('请输年龄:'))
b = input('请输入性别:')
if ((a>=22)and(b=='男'))or((a>=20)and(b=='女')):
	print('能结婚')
else:
	print('不能结婚')
'''

'''
a = input('请输姓名:')
b = input('请输密码:')
if (a=='老李')and(b=='123'):
	print('登陆成功')
else:
	print('登录失败')
'''

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
a = 1
while a < 20:
	print(a)
	a += 1
	if(a==10):
		break
print('结束')