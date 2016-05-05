#打印乘法表
n = 9
while n>=1:
	m = 1
	while m<=n:
		print('%s*%s=%s\t'%(m,n,n*m),end='')
		m+=1
	print()
	n-=1


