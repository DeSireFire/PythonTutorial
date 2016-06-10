from threading import *

myLocal = local()

def a(name):
    std = name
    myLocal.b = std
    b()

def b():
    print(myLocal.b)

if __name__ == '__main__':
    t1 = Thread(target=a,args=("老王",))
    t2 = Thread(target=a,args=("老李",))
    t1.start()
    t2.start()