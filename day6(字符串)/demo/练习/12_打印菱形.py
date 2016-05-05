#打印菱形
n = int(input('请输入奇数:'))
i = 1
while i<=(n+1)/2:
	print(' '*int((n+1)/2-i),end='')
	print('*'*(2*i-1))
	i += 1
j = 1
while j<=(n-1)/2:
	print(' '*int(j),end='')
	print('*'*(n-2*j))
	j+=1

