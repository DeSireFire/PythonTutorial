'''
九九乘法表
n*m=结果
'''


m = 1			#第几次循环，第几行		
n = 1			#这一行，打印几次
while m<10:
	while n<=m:
		print('%sx%s=%s\t'%(n,m,m*n),end='')
		n+=1
	print('')
	n=1
	m+=1



'''

print('老王',end='')
print('旺财')
'''



'''
print('老王\t旺财')
\n换行
\t制表位
'''