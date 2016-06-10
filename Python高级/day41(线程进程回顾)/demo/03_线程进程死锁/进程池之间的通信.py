import time,random,os
from multiprocessing import Pool,Manager

def writer(q):
    print("writer启动(%s),父进程为(%s)"%(os.getpid(),os.getppid()))
    for i in "yongGe":
        q.put(i)
def reader(q):
    print("reader启动(%s),父进程为(%s)"%(os.getpid(),os.getppid()))
    for i in range(q.qsize()):
        print("reader从Queue获取到消息：%s"%q.get())

if __name__ == '__main__':
    print("%s开始"%os.getpid())
    q = Manager().Queue()#使用Manager中的Queue来初始化
    po = Pool()
    # 使用阻塞模式创建进程，这样就不需要在reader中使用死循环了，
    # 可以让writer完全执行完成后，再用reader去读取
    po.apply(writer,(q,))
    po.apply(reader,(q,))
    po.close()
    po.join()
    print("%s结束"%os.getpid())

# 2485开始
# writer启动(2491),父进程为(2485)
# reader启动(2491),父进程为(2485)
# reader从Queue获取到消息：y
# reader从Queue获取到消息：o
# reader从Queue获取到消息：n
# reader从Queue获取到消息：g
# reader从Queue获取到消息：G
# reader从Queue获取到消息：e
# 2485结束