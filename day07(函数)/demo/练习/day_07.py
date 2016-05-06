'''
def ss(a,b):
	max = a
	if max<b:
		max = b
	return max
ret = ss(12,54)
t = ss(12,7)
print(ret)
print(t)


def a(aa,bb,cc):
	print('你是傻狗!!!')
	if(aa<bb):
		aa = bb
	b(aa)
	print('a函数结束!!!')
def b(num):
	print('结果出来啦%s'% num)
a(25,40,36)
'''
'''
def a(l):
	l.append(10)
	print(l)
ss = [1,2,3]
a(ss)

def a(l):
	l = 10
	print(l)
ss = [1,2,3]
a(ss)

def a(name='小王',age=10):
	print('name=%s,age=%s'%(name,age))
a('老王',20)
a('老王')
a(256)
a(age='52')

def m(*num):
	print(type(num))
	print(num)
m(1,2,3,4,[8,5,6],{78,98,564,45})

def k(*num):
	print(sum(num))
k(1,5,6,4)

ls=[1,2,3,4]
k(ls[0],ls[1],ls[2],ls[3])
k(*ls)

def ll(**m):
	print(m)

ll(sid=1,name='老王',age=20)

def la(*args,**kwargs):
	print(args)
	print(kwargs)
la(1,'小王',sid=1,name='老王',age=20)
la(1,'小王','nani')
'''
'''
	局部变量和全局变量
	局部变量就是定义在函数内部的变量,
		局变量能调用全局变量但是，无法修改全局变量
			如果在函数中修改全局变量，那么就需要使用global进行声明
	全局变量就是定义在函数外边的变量

	如果全局变量的名字和局部变量的名字相同，那
		么使用的是局部变量

'''
'''
num = 100
def la(m):
	m+=100
	print('函数内部使用的结果是:%s'%m)
la(num)
print(num)

num = 100
def la():
	global num
	num+=100
	print('函数内部使用的结果是:%s'%num)
la()
print(num)

num = 100
def la(m):
	m+=100
	print('函数结果是:%s'%m)
la(145)
print(num)

num1=1000
def la():
	
	print('函数内部使用的结果是:%s'%num1)
la()
print(num1)
'''
'''
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