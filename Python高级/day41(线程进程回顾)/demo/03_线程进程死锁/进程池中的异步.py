from multiprocessing import Pool
import time,os

def a():
    print("进程池中的进程pid=%s,ppid=%s"%(os.getpid(),os.getppid()))
    for i in range(3):
        print("%d"%i)
        time.sleep(1)
    return "haha"

def b(num):
    print("callback   pid=%s"%os.getpid())
    print("callback   args=%s"%num)

if __name__ == '__main__':
    pool = Pool(3)
    #主进程3959
    #callback   pid=3959
    #callback   args=haha
    pool.apply_async(func=a,callback=b)
    time.sleep(3)
    print("主进程%s"%os.getpid())

# 进程池中的进程pid=2457,ppid=2455
# 0
# 1
# 2
# 主进程2455
# callback   pid=2455
# callback   args=haha