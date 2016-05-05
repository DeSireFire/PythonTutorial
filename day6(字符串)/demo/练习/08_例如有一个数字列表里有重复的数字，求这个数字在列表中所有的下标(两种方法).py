
#例如有一个数字列表里有重复的数字，求这个数字在列表中所有的下标
a = [2,1,3,5,6,9,5,7,5,8,4,5]
r = 0
for n in a:
	if a.count(n)>1:
		r = n
k = 0
while k<len(a):	
	if a[k]==r:
		print('%s '%k,end='')
	k+=1

print()
print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")

#第二种
i = 0
while i<len(a):
	if(a.count(a[i])>1):
		print('%s '%i,end='')
	i+=1
#统计字符串中，各个字符的个数
print()
m = input('输入字符串:').strip()
print()
b = list(m)
a = {}
for i in b:
	a[i]=b.count(i)
print(a)

