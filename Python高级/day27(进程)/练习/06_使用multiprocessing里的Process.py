import os
import time
from multiprocessing import Process

def run_proc2(num):
    print('子进程运行中...')
    time.sleep(5)
    print('子进程中，num= %s ,pid=%d...' % (num, os.getpid()))
    print('子进程结束...')

def run_proc1():
    print('子进程运行中...，,pid=%d...' % (os.getpid()))
    time.sleep(3)
    print('end1...')

def f1():
    print('1子进程运行中...，,pid=%d...' % (os.getpid()))
    time.sleep(10)

def f2():
    print('2子进程运行中...，,pid=%d...' % (os.getpid()))

def f3():
    print('3子进程begin...')
    print('3子进程运行中...，,pid=%d...' % (os.getpid()))
    time.sleep(10000)
    print('3子进程end...')


def test1():
    print('父进程 %d.' % os.getpid())
    """
        daemon=True设置为True，表示是守护进程。
        进程：普通进程和守护进程
        如果程序中只剩下守护进程，程序结束。
        如果有剩余的普通进程，等待执行完毕之后，再结束程序
    """
    """
        进程的状态：
        1.Process(target=run_proc1)初始化状态
        2.p1.start()就绪状态，等待获取cpu的使用权
        3.进程的功能函数执行中，运行状态
        4.进程的功能函数执行完，消亡状态
        5.进程的功能函数执行中,sleep,阻塞状态
    """
    # p1 = Process(target=run_proc1,daemon=True)
    p1 = Process(target=run_proc1)
    print('子进程将要执行...')
    p1.start()
    print('end...')

def test2():
    print('父进程 %d.' % os.getpid())
    p1 = Process(target=run_proc2,name="laowang",args=(10,))
    print('子进程将要执行...')
    p1.start()
    p1.join()
    print('end...pid=%s'%(os.getpid()))

def test3():
    print('父进程 %d.' % os.getpid())
    p1 = Process(target=f1)
    p2 = Process(target=f2)
    p1.start()
    time.sleep(4)
    print(p1.is_alive())
    p2.start()
    p1.join()
    # p1.join(5)
    print('end...pid=%s' % (os.getpid()))
    print(p1.is_alive())

def test4():
    print('父进程 %d.' % os.getpid())
    p1 = Process(target=f3)
    p1.start()
    p1.terminate()
    time.sleep(4)
    print(p1.is_alive())

if __name__ == '__main__':
    #test1()
    #test2()
    #test3()
    test4()

