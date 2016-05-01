'''
	外层循环循环一次，内层循环执行完毕
'''

m = 1
n = 1
while m<11:
	print('m=%s'%m)
	m+=1
	while n<5:
		print('n=%s'%n)
		n+=1
	n=1
	print('。。。。')