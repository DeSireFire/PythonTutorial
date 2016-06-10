from threading import Thread
import time

def a(num):
    num.append(44)
    print("aaaaaaaaaaaaa%s"%num)

def b(num):
    time.sleep(2)
    print("bbbbbbbbbbbbb%s"%num)

lis = [11,22,33]

t1 = Thread(target=a,args=(lis,))
t1.start()

t2 = Thread(target=b,args=(lis,))
t2.start()