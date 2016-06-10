import threading
from time import sleep,ctime

def sing():
    for i in range(8):
        print("%d正在唱歌"%i)
        sleep(1)

def dance():
    for i in range(8):
        print("%d正在跳舞"%i)
        sleep(1)

if __name__ == '__main__':

    print("开始%s"%ctime())

    t1 = threading.Thread(target=sing)
    t2 = threading.Thread(target=dance)

    t1.start()
    t2.start()

    print("结束%s"%ctime())

    while True:
        length = len(threading.enumerate())
        print("当前线程数为:%s"%length)
        if length<=1:
            break
        sleep(0.5)