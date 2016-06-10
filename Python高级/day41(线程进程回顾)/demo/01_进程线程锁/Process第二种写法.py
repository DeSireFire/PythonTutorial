from multiprocessing import Process
import time
import os

class Myprocess(Process):
    #deamon守护进程
    def __init__(self,a,daemon):
        # 调用父类的__init__为了初始化父类的属性，让对象完整
        #Process.__init__(self,daemon = daemon)
        Process.__init__(self, daemon=daemon)
        self.a = a
    #重写的是父类Prosess的run方法，当进程对象start之后，并获取cpu的使用权之后，立即调用
    def run(self):
        print("子进程%s开始执行，父进程为%s"%(os.getpid(),os.getppid()))
        start = time.time()
        time.sleep(self.a)
        stop = time.time()
        print("%s执行结束，耗时%0.2f秒"%(os.getpid(),stop-start))

def test():
    start1 = time.time()
    print("当前进程为:%s"%os.getpid())
    #创建进程对象
    p1 = Myprocess(2,True)
    #通过继承Prosess实现多进程，进程对象执行start()方法，就会运行这个类中的run()方法，所以这里会执行p1.run()
    p1.start()
    p1.join()
    stop1 = time.time()
    print("%s执行结束，耗时%0.2f"%(os.getpid(),stop1-start1))

if __name__ == "__main__":
    test()