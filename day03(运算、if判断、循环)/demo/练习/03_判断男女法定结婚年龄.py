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

a = int(input('请输年龄:'))
b = input('请输入性别:')
if ((a>=22)and(b=='男'))or((a>=20)and(b=='女')):
	print('能结婚')
else:
	print('不能结婚')

