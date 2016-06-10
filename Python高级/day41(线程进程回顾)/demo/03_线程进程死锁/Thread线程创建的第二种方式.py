import time,os
from threading import Thread,enumerate

class MyThread(Thread):

    def __init__(self,name):
        Thread.__init__(self,name = name)

    def run(self):
        self.myRun()

    def myRun(self):
        print('线程运行中...')
        time.sleep(3)
        print('线程结束...')


if __name__ == '__main__':
    print("进程%s"%os.getpid())
    t1 = MyThread("我的线程")
    t1.start()
    t1.join()
    print(t1.getName())
    print(enumerate)
