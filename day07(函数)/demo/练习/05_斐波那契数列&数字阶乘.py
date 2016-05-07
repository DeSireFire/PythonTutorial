#斐波那契数列

def a(can):
	if can==1 or can==2:
		return 1
	return a(can-1)+a(can-2)
#n = int(input('请输入值:').strip())
#print(a(n))
def ja(m):
	m1,m2,m3 = 1,1,1
	if m<1:
		print('输入错误')
		return -1
	while (m-2)>0:
		m3 = m2 + m1
		m1 = m2
		m2 = m3
		m-=1
	return m3
print(ja(6))


#数字阶乘
def jie(m):
	if m == 1:
		return 1
	return m * jie(m-1)
n = int(input('请输入值:').strip())
print(jie(n))

def ff(m):
	ret = 1
	for n in range(2,m+1):
		ret*=n
	return ret
n = int(input('请输入值:').strip())
print(ff(n))
'''
f1 = lambda a,b:a*b
print(f1(2,3))

f2 = lambda ls:ls.append(119)
ls = [110,120,111]
f2(ls)
print(ls)
print(f2(ls))

def ll(func):
	ret = func(2,6)
	print(ret)

def ha(a,b):
	return a*b
ll(ha)
k = lambda a,b:a*b
print(k(5,9))

ka = 'fjkdshkfj'
print(ka[:])
print(ka[:5])
print(ka[1:5])
print('&&&&&&&')
print(ka[:-1])
print(ka[-1:])
print('&&&&&&&')
print(ka[1:-1])
print(ka[:-4])
