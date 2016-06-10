import os,time
from multiprocessing import Process

# 通过继承Process实现多进程，进程对象执行start()方法，
# 就会运行这个类中的run()方法，所以这里会执行p1.run()
class myP(Process):
    def __init__(self,num):
        Process.__init__(self)
        self.num = num

     # 重写的是父类Process的run方法，当进程对象start之后，并获取cpu的使用权上之后，立刻调用
    def run(self):
        print("子进程%s开始执行，父进程为：%s"%(os.getpid(),os.getppid()))
        start = time.time()
        time.sleep(self.num)
        end = time.time()
        print("%s执行结束，用时%0.3f" % (os.getpid(), end - start))

def test():
    start = time.time()
    print("当前进程%s"%os.getpid())
    #创建进程对象
    p1 = myP(3)
    p1.start()
    p1.join()
    end = time.time()
    print("%s执行结束，用时%0.3f"%(os.getpid(),end-start))

if __name__ == '__main__':
    test()