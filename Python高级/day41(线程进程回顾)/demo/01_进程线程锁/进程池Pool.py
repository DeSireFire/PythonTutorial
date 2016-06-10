import os,time,random
from multiprocessing import Pool

def worker(msg):
    start = time.time()
    print("%s开始执行，进程号为%d"%(msg,os.getpid()))
    time.sleep(random.random()*3)
    stop = time.time()
    print("执行完毕，耗时%0.2f"%(stop-start))

po = Pool(3)
for i in range(0,8):
    # po.apply_async(worker,(i,))
    po.apply(worker, (i,))
