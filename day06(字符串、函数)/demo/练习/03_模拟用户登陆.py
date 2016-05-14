'''
设计一个验证用户密码程序，用户只有三次机会输入错误。如果输入对了，打印登录成功
'''

'''
switch = True
i=0
while switch:
	i+=1
	password = input('请输入密码：')
	if password=='123456':
		print('登录成功！')
		switch=False
	elif i>2:
		switch=False
		print('输入错误超过三次，账号被锁定！')
'''


for i in range(3):
	password = input('请输入密码：')
	if password=='123456':
		print('登录成功！')
		break
	else:
		print('输入错误，请再试试。')
		if i==2:
			print('输入错误超过三次，账号被锁定！')
				
