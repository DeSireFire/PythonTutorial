from multiprocessing import Process
import os
import time

#子进程要执行的代码
def run_proc(name):
    print("子进程运行中，name=%s,pid=%d"%(name,os.getpid()))
def test1():
    print("父进程%d" % os.getpid())
    p = Process(target=run_proc, args=("test",))
    print("子进程将要执行")
    p.start()
    p.join()
    print("子进程结束")
def one(name):
    print("子进程运行中。。。")
    time.sleep(5)
    print("子进程中，num=%s,pind=%s"%(name,os.getpid()))
def test2():
    print("父进程%d"%os.getpid())
    p1 = Process(target=one,name="laowang",args=(10,))
    print("子进程将要执行")
    p1.start()
    p1.join()
    print("end....pid=%s"%os.getpid())

def two():
    print("子进程1运行中pid=%s"%os.getpid())
    time.sleep(5)
def two1():
    print("子进程1运行中pid=%s"%os.getpid())
def test3():
    print("父进程%d"%os.getpid())
    p1 = Process(target=two)
    p2 = Process(target=two1)
    p1.start()
    time.sleep(4)
    print(p1.is_alive())
    p2.start()
    p1.join()
    print("end...pid=%s"%os.getpid())
    print(p1.is_alive())

def three():
    print("3子进程开始运行。。。")
    print("3子进程运行中。。。pid=%"%os.getpid())
    time.sleep(1000)
    print("3子进程结束")
def test4():
    print("父进程%d"%os.getpid())
    p1 = Process(target=three)
    p1.start()
    p1.terminate()#杀死结束进程
    time.sleep(4)
    print(p1.is_alive())
if __name__ == "__main__":
    # test1()
    # test2()
    # test3()
    test4()