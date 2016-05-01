'''
	1、1-100之间能被3整除的数的和
'''
num = 1
ret = 0
while num<101:
	if num%3==0:
		ret = ret+num
	num+=1
print(ret)


'''
	2、存款金额的1万，年利率是0.35%，从2017年开始，到哪一年，存款会达到2万
'''
num = 1
year = 2017
rate = 0.0035
while num<2:
	year+=1
	num = num*(1+rate)
print(year)