import functools

def showarg(*args, **kw):
    print(args)
    print(kw)

p1=functools.partial(showarg, 1,2,3)

p1()

print('************************************华丽的分割线************************************')

p1('老王',name='xx')

#showarg(1,2,3,'老王',name='xx')

print('************************************华丽的分割线************************************')


'''
def f(a,b):
	print('a=%s,b=%s'%(a,b))

p=functools.partial(f, 1,2)

p(10,20)
'''