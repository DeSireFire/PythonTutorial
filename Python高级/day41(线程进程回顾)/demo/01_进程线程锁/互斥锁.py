from threading import Thread,Lock
import time

num = 0

def test1():
    global num
    for i in range(100000):
        mutexFlag = mutex.acquire(True)
        if mutexFlag:
            num += 1
            mutex.release()

    print("test1----num=%d"%num)

def test2():
    global num
    for i in range(100000):
        mutexFlag = mutex.acquire(True)
        if mutexFlag:
            num += 1
            mutex.release()

    print("test2----num=%d"%num)

mutex = Lock()


p1 = Thread(target=test1)
p1.start()

p2 = Thread(target=test2())
p2.start()

print("--num=%d--"%num)