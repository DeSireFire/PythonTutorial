'''
#打印乘法表
n = 9
while n>=1:
	m = 1
	while m<=n:
		print('%s*%s=%s\t'%(m,n,n*m),end='')
		m+=1
	print()
	n-=1
'''
'''
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
'''

'''
s = "aAsmr3idd4bgs7Dlsf9eAF"
1.请将s字符串的数字取出，并输出成一个新的字符串。
2.请统计s字符串出现的每个字母的出现次数（忽略大小写，a与A是同一个字母），
  并输出成一个字典。 例 {'a':3,'b':1}
3.请去除s字符串多次出现的字母，仅留最先出现的一个,大小写不敏感。
  例 'aAsmr3idd4bgs7Dlsf9eAF'，经过去除后，输出 'asmr3id4bg7lf9e'
4.输出s字符串出现频率最高的字母。
'''
'''
#1.0
s = "aAsmr3idd4bgs7Dlsf9eAF"
a = list(s)
for i in a:
	if i.isdigit():
		a.remove(i)
d = ''.join(a)
print(d)
#2.0
d.lower()
m = list(d)
b = {}
for k in d:
	b[k]=m.count(k)
print(b)
#3.0
s = s.lower()
aa = list(s)
max=1
for i in aa:
	if aa.count(i)>max:
		max = aa.count(i)
aa.reverse()
mm = 1
while mm<max:
	for m in aa:
		if aa.count(m)>1:
			aa.remove(m)
	mm+=1
aa.reverse()
bb = ''.join(aa)
print(bb)

#4.0

aa = list(s)
max=1
for i in aa:
	if aa.count(i)>max:
		max = aa.count(i)
		print(i,'\000',end='')

#斐波那契数列
def c(m):
	if m == 1 or m == 2:
		return 1
	return c(m-1)+c(m-2)
print()
print(c(10))

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
'''
'''
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
'''
'''
存放家具
'''
'''
class home:
	def __init__(self,daxiao,jiajus=None):
		jiajus=[]
		self.daxiao = daxiao
		self.jiajus = jiajus
	def __str__(self):
		num = self.daxiao
		for n in self.jiajus:
			num += n.daxiao
		msg = '家庭总面积:%s,家庭剩余总面积:%s'%(num,self.daxiao)

		return msg
	def cunfang(self,jiaju):
		if self.daxiao>jiaju.daxiao:
			self.jiajus.append(jiaju)
			self.daxiao-=jiaju.daxiao
		else:
			print('空间不够，存储不下了!!!')
class jia:
	def __init__(self,name,daxiao):
		self.name = name
		self.daxiao = daxiao
	def __str__(self):
		msg = '家具名字:%s,家具大小:%s'%(self.name,self.daxiao)
		return msg
hh = home(120)
ll = jia('电脑',5)
hh.cunfang(ll)
print(hh)
print(ll)

hh1 = home(110)
ll1 = jia('麻将桌',10)
hh1.cunfang(ll1)
print(hh1)
print(ll1)
'''
