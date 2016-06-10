import threading
import time

class MyThread(threading.Thread):

    def __init__(self,num,sleepTime):

        threading.Thread.__init__(self)
        self.num = num
        self.sleepTime = sleepTime

    def run(self):
        self.num += 1
        time.sleep(self.sleepTime)
        print("线程%s,num=%d"%(self.name,self.num))

if __name__ == '__main__':
    # mutex = threading.Lock()
    t1 = MyThread(100,3)
    t1.start()
    t2= MyThread(200, 1)
    t2.start()