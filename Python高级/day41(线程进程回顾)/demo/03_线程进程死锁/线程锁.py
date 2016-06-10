from threading import Thread,enumerate,Lock
import time,threading

num = 0
lock = Lock()

def one():
    global num
    isLock = lock.acquire()
    if isLock:
        for i in range(100000):
            num += 1
        print("one.....%s" % num)
        lock.release()

def two():
    global num
    isLock = lock.acquire()
    if isLock:
        for i in range(100000):
            num+=1
        print("two.....%s" % num)
        lock.release()
def test(sleepTime):
    num=1
    time.sleep(sleepTime)
    num+=1
    print('---(%s)--num=%d'%(threading.current_thread(), num))

if __name__ == '__main__':
    p1 = Thread(target=one)
    p1.start()

    p2 = Thread(target=two)
    p2.start()

    print(enumerate())
    print(num)

    t1 = Thread(target=test, args=(2,))
    t2 = Thread(target=test, args=(1,))

    t1.start()
    t2.start()