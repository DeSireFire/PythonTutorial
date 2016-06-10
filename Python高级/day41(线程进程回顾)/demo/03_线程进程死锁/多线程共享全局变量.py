import time
from threading import Thread

def one(b):
    b.append(55)
    print(b)
def two(b):
    time.sleep(5)
    print(b)

if __name__ == '__main__':
    a = [11,22,33]
    t1 = Thread(target=one,args=(a,))
    t1.start()
    t2 = Thread(target=two,args=(a,))
    t2.start()