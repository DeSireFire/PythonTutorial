import os
import time
from threading import Thread,enumerate

def myRun():
    print('线程运行中...')
    time.sleep(3)
    print('线程结束...')


class MyThread(Thread):

    def __init__(self,tname):
        Thread.__init__(self,name = tname)

    def run(self):
        self.myRun()
    def myRun(self):
        print('线程运行中...')
        time.sleep(3)
        print('线程结束...')



if __name__ == '__main__':
    print('进程 %d.' % os.getpid())
    t1 = MyThread('老王的线程')
    t1.start()
    t1.join()
    print(t1.getName())
    print(enumerate())
    print('game over...')
