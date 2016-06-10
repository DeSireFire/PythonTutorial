import os
import time

a = 0

num = os.fork()

if num == 0:
    a += 1
    # print("1进程", a)
    print("进程1本身ID%s父进程ID%s",(os.getpid(),os.getppid()))
else:
    # time.sleep(3)
    a += 1
    # print("2进程", a)
    print("进程2本身ID%s父进程ID%s",(os.getpid(),os.getppid()))

num = os.fork()

if num == 0:
    a += 1
    # print("3进程",a)
    print("进程3本身ID%s父进程ID%s",(os.getpid(),os.getppid()))
else:
    a += 1
    # print("4进程", a)
    print("进程4本身ID%s父进程ID%s",(os.getpid(),os.getppid()))