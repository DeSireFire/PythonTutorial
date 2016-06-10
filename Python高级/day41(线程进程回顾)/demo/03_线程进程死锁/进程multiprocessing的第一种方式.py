from multiprocessing import Process
import time,os

def one():
    print("子进程运行中")
    time.sleep(2)
    print("子进程,pid=%s"%os.getpid())

def two(num):
    print("子进程运行中")
    time.sleep(2)
    print("子进程num=%s,pid=%s" % (num, os.getpid()))

def test():
    print("父进程pid%s"%os.getpid())
    p1 = Process(target=one)
    p2 = Process(target=two,args=(110,))
    p1.start()
    p1.join()
    print(p1.is_alive())
    time.sleep(5)
    p2.start()
    #p2.terminate()
    print(p2.is_alive())
    p2.join()



if __name__ == '__main__':
    test()