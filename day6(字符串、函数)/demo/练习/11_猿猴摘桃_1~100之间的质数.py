#猿猴摘桃子
def num(day):
	sum = 1
	while day>0:
		sum = (sum+1)*2
		day-=1
	return sum
print(num(9))

#1~100之间的质数
num = list(range(2,101))
i = 2
while i<101:
	for n in num:
		if n%i==0 and n>i:
			num.remove(n)
	i+=1
print(num)

