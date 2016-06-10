import threading
import time
import os

def doChore():
    time.sleep(0.2)

def booth(tid):
    global i
    global lock
    while True:
        lock.acquire()
        if i != 0:
            i = i-1
            print(tid,':now left:',i)
            doChore()
        else:
            print("Thread_id",tid,"No More Tick")
            os._exit(0)
        lock.release()
        doChore()

i = 15
lock = threading.Lock()

def main():
    for k in range(3):
        new_thread = threading.Thread(target=booth,args=(k+1,))
        new_thread.start()

if __name__ == '__main__':
    main()