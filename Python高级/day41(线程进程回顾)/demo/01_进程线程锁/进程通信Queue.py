from multiprocessing import Queue,Process
import  os,time,random

def write(q):
    for i in [1,2,3,4]:
        print("Put %s to queue..."%i)
        q.put(i)
        time.sleep(random.random())

def read(q):
    a = True
    while a:
        if not q.empty():
            i = q.get()
            print("Get %s to queue..." % i)
            time.sleep(random.random())



if __name__ == '__main__':

    q  = Queue()

    pw = Process(target=write,args=(q,))
    pr = Process(target=read, args=(q,))

    pw.start()
    #pw.join()

    pr.start()
    #pr.join()

    print("end....")
