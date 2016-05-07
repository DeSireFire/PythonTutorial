# 函数对变量的操作
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

