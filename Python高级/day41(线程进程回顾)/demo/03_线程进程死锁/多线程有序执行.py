import threading,time

class test1(threading.Thread):
    def run(self):
        while True:
            if lock1.acquire():
                print("test1")
                time.sleep(1)
                lock2.release()

class test2(threading.Thread):
    def run(self):
        while True:
            if lock2.acquire():
                print("test2")
                time.sleep(1)
                lock3.release()

class test3(threading.Thread):
    def run(self):
        while True:
            if lock3.acquire():
                print("test3")
                time.sleep(1)
                lock1.release()

if __name__ == '__main__':

    lock1 = threading.Lock()
    lock2 = threading.Lock()
    lock2.acquire()
    lock3 = threading.Lock()
    lock3.acquire()

    t1 = test1()
    t2 = test2()
    t3 = test3()

    t1.start()
    t2.start()
    t3.start()

