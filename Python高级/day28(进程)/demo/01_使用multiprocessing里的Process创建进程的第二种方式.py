import os
import time
from multiprocessing import Process

class Myprocess(Process):
    def __init__(self, interval):
        #调用父类的__init__为了初始化父类的属性，让对象完整
        Process.__init__(self)
        self.interval = interval
    #重写的是父类Process的run方法，当进程对象start之后，并获取cpu的使用权上之后，立刻调用
    def run(self):
        print("子进程(%s) 开始执行，父进程为（%s）" % (os.getpid(), os.getppid()))
        t_start = time.time()
        time.sleep(self.interval)
        t_stop = time.time()
        print("(%s)执行结束，耗时%0.2f秒" % (os.getpid(), t_stop - t_start))


def test1():
    t_start = time.time()
    print("当前程序进程(%s)" % os.getpid())
    #创建一个进程对象
    p1 = Myprocess(2)
    # 通过继承Process实现多进程，进程对象执行start()方法，就会运行这个类中的run()方法，所以这里会执行p1.run()
    p1.start()  #错误的写法 p1.run()
    p1.join()
    t_stop = time.time()
    print("(%s)执行结束，耗时%0.2f" % (os.getpid(), t_stop - t_start))


if __name__ == '__main__':
    test1()

