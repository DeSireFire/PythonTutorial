from threading import Thread,enumerate,Lock
import time

g_num = 0
g_lock = Lock()

def test1():
    global g_num
    for i in range(1000000):
        isLock = g_lock.acquire()
        if isLock:
            g_num += 1
            g_lock.release()

    print("---test1---g_num=%d"%g_num)

def test2():
    global g_num
    for i in range(1000000):
        isLock = g_lock.acquire()
        if isLock:
            g_num += 1
            g_lock.release()

    print("---test2---g_num=%d"%g_num)


p1 = Thread(target=test1)
p1.start()


p2 = Thread(target=test2)
p2.start()

print(enumerate())

print("---g_num=%d---"%g_num)
