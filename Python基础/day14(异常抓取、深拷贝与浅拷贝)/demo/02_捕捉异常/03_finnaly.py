'''
try:
	...
except:
	...
else:
	...
finally:
	...
'''


print('begin...')
file = None
try:
	print('1...')
	a+=1
	file = open(r'C:\Users\Administrator\Desktop\软件\老王.txt','r')
	num = 1/0
	print('2...')
except Exception as ex:
	print('出现异常了:%s'%ex)
else:
	print('else...')
finally:
	print('finally...')
	if file!=None:
		file.close()
print('end...')