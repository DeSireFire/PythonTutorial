from threading import Thread,enumerate,Lock
import time

g_num = 0
g_lock = Lock()

def test1():
    time.sleep(10)
    global g_num
    isLock = g_lock.acquire()
    if isLock:
        for i in range(1000000):
            g_num += 1
        print("---test1---g_num=%d" % g_num)
        g_lock.release()



def test2():
    global g_num
    isLock = g_lock.acquire()
    if isLock:
        for i in range(1000000):
            g_num += 1
        print("---test2---g_num=%d" % g_num)
        g_lock.release()
    else:
        print('---test2---没有获取到锁,那我就走了')




p1 = Thread(target=test1)
p1.start()


p2 = Thread(target=test2)
p2.start()

print(enumerate())

print("---g_num=%d---"%g_num)
