from threading import Thread
import time

num = 0

def test1():
    global num
    for i in range(1000000):
        num += 1

    print("test1  num=%s"%num)

def test2():
    global num
    for i in range(1000000):
        num += 1

    print("test2 num=%s"%num)

p1 = Thread(target=test1)
p1.start()

#time.sleep(3)

p2 = Thread(target=test2())
p2.start()