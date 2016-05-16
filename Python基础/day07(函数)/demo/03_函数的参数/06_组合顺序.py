'''
	顺序：
		必选，默认，可变
'''

def f(name,age=18,*args,**kvargs):
	print(name,age,args,kvargs)

f('老王')
f('老王',20)
f('老王',20,110,'abc')
f('老王',20,110,'abc',sid=1,num=20)
