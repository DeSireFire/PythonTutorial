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

read = int(input('请输入年份:'))
if ((read%4==0) and (read%100!=0)) or (read%400==0):
	print('%d是闰年'%(read))
else:
	print('%d不是闰年'%(read))
print('判断结束')

