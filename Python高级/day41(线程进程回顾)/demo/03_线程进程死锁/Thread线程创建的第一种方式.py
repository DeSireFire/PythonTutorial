import os,time
from threading import Thread,enumerate

def one():
    print("线程开始")
    time.sleep(3)
    print("线程结束")

if __name__ == '__main__':
    print("%s线程"%os.getpid())
    t1 = Thread(target=one)
    t1.start()
    print(t1.getName())
    print(enumerate())
