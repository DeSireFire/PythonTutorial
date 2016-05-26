import time,random
from multiprocessing import Process,Queue


def write(q):
    print('write...%s' % (id(q)))
    for value in ['A', 'B', 'C']:
        print('Put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())

def read(q):
    print('read...%s,num=%s,flag = %s'%(id(q),q.qsize(),q.empty()))
    while True:
        if not q.empty():
            value = q.get()
            print('Get %s from queue.' % value)
            time.sleep(3)

if __name__ == '__main__':
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    # 启动子进程pw，写入:
    pw.start()
    # 等待pw结束:
    #pw.join()
    # 启动子进程pr，读取:
    pr.start()
    #pr.join()

    print('game over...')