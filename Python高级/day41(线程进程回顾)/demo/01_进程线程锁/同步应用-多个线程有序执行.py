from threading import Thread,Lock
from time import sleep

class Task1(Thread):
    def run(self):
        while True:
            if lock1.acquire():
                print("Task1")
                sleep(0.5)
                lock2.release()
class Task2(Thread):
    def run(self):
        while True:
            if lock2.acquire():
                print("Task2")
                sleep(0.5)
                lock3.release()
class Task3(Thread):
    def run(self):
        while True:
            if lock3.acquire():
                print("Task3")
                sleep(0.5)
                lock1.release()

lock1 = Lock()
#创建另外一把锁，并且“锁上”
lock2 = Lock()
lock2.acquire()
#创建另外一把锁，并且“锁上”
lock3 = Lock()
lock3.acquire()

t1 = Task1()
t2 = Task2()
t3 = Task3()

t1.start()
t2.start()
t3.start()