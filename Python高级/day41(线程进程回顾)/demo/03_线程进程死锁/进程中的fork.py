import os
import time

num = os.fork()
if num==0:
    print("进程1:%s，父进程%s"%(os.getpid(),os.getppid()))
else:
    print("进程2:%s，父进程%s"%(os.getpid(),os.getppid()))
num1 = os.fork()
if num1==0:
    print("进程3:%s，父进程%s"%(os.getpid(),os.getppid()))
else:
    print("进程4:%s，父进程%s"%(os.getpid(),os.getppid()))

num = 0

pid = os.fork()

if pid == 0:
    num+=1
    print('哈哈1---num=%d'%num)
else:
    time.sleep(5)
    num+=1
    print('哈哈2---num=%d'%num)
# 进程2:2433，父进程2060
# 进程4:2433，父进程2060
# 哈哈1---num=1
# 进程3:2435，父进程2433
# 进程1:2434，父进程2433
# 进程4:2434，父进程2433
# 哈哈1---num=1
# 进程3:2438，父进程2434
# 哈哈1---num=1
# 哈哈1---num=1
# 哈哈2---num=1
# 哈哈2---num=1
# 哈哈2---num=1
# 哈哈2---num=1