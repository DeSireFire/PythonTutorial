from time import ctime, sleep

def timefun(func):
    def wrappedfunc(*args,**kwargs):
        print("%s called at %s"%(func.__name__, ctime()))
        func(*args,**kwargs)
    return wrappedfunc

@timefun
def foo1(a,b):
    print(a+b)

@timefun
def foo2(a, b, c):
    print(a+b+c)

@timefun
def foo3(a, b, c,d):
    print(a+b+c+d)


'''
调用者
'''
foo1(1,2)
foo2(1,2,3)