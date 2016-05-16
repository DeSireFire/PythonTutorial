from time import ctime, sleep

def timefun(func):
    def wrappedfunc(a,b):
        print("%s called at %s"%(func.__name__, ctime()))
        func(a,b)
    return wrappedfunc

@timefun
def foo(a,b):
    print(a+b)


'''
调用者
'''
foo(1,2)
