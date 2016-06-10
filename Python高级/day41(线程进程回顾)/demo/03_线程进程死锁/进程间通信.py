from multiprocessing import Queue,Process
import time,random


def one(q):
    print("write..%s"%id(q))
    for i in ['1','2','3']:
        q.put(i)
        time.sleep(random.random())

def two(q):
    print("read...%s,num=%s,flag=%s"%(id(q),q.qsize(),q.empty()))
    while True:
        if not q.empty():
            value = q.get()
            print('Get %s from queue.' % value)
            time.sleep(2)

if __name__ == '__main__':
    q = Queue()
    pw = Process(target=one,args=(q,))
    pr = Process(target=two,args=(q,))
    pw.start()
    pr.start()
    print("结束")
# 结束
# write..140226239163752
# read...140226239163752,num=1,flag=False
# Get 1 from queue.
# Get 2 from queue.
# Get 3 from queue.