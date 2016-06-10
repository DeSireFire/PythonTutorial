import threading
from time import sleep

def one(num):
    a = 1
    sleep(num)
    #current_thread()当前线程变量
    print("....%s.....num=%s...."%(threading.current_thread(),a))

if __name__ == '__main__':
    t = threading.Thread(target=one,args=(5,))
    t1 = threading.Thread(target=one,args=(2,))
    t.start()
    t1.start()
