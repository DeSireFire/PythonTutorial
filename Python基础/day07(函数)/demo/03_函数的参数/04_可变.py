'''
	可变元组
	可变字典

	注意：
		可变元组 在 可变字典  之前
'''

def f(a,b):
	print(a+b)

f(1,2)

def f(a,b,c):
	print(a+b+c)

f(1,2,3)


def f(*num):
	print(type(num))
	print(num)

f(1,2,3,4,5,[1,2],{'id':1,'name':'x'})


def f(*num):
	print(sum(num))

f(1,2,3)

ls=[1,2,3]
f(ls[0],ls[1],ls[2])

f(*ls)

f()



def f(**num):
	print(num)


f(id=1,name='老王')


def f(sid,**num):
	print(num)


f(sid=1,name='老王')


def f(*args,**kvargs):
	print(args)
	print(kvargs)


f(1,'老王',sid=1,name='老王')


