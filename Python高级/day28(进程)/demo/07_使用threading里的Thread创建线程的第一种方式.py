import os
import time
from threading import Thread,enumerate

def myRun():
    print('线程运行中...')
    time.sleep(3)
    print('线程结束...')






if __name__ == '__main__':
    print('进程 %d.' % os.getpid())
    t1 = Thread(target=myRun)
    t1.start()
    print(t1.getName())
    print(enumerate())
    print('game over...')
