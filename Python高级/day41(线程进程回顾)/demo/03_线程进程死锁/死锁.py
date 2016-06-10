import threading,time

class myThread1(threading.Thread):
    def run(self):
        if mutexA.acquire():
            print(self.name)
            time.sleep(2)
            if mutexB.acquire():
                print(self.name)
                mutexB.release()
            mutexA.release()

class myThread2(threading.Thread):
    def run(self):
        if mutexB.acquire():
            print(self.name)
            if mutexA.acquire():
                print(self.name)
                mutexA.release()
            mutexB.release()

mutexA = threading.Lock()
mutexB = threading.Lock()

if __name__ == '__main__':
    t1 = myThread1()
    t2 = myThread2()
    t1.start()
    t2.start()