from threading import Thread
import time

num = 100

def work1():
    global num
    for i in range(3000):
        num+=1
    print("----in work1, g_num is %d---" % num)
def work2():
    global num
    for i in range(3000):
        num+=1
    print("----in work1, g_num is %d---" % num)

t1 = Thread(target=work1)
t1.start()

# time.sleep(3)

t2 = Thread(target=work2)
t2.start()