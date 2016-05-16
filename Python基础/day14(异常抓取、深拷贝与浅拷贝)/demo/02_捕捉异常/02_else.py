'''
...
try:
	...
except:
	...
else:
	...
...

'''


print('begin...')
try:
	print('1...')
	#num=110
	file = open(r'C:\Users\Administrator\Desktop\软件\老王.txt','r')
	print('2...')
except Exception as ex:
	print('出现异常了1:%s'%ex)
else:
	print('else...')
	file.close()
	#print(num)
print('end...')