import os
import time

#全局变量
num = 0

pid = os.fork()

if pid == 0:
    num+=1
    print('哈哈1---num=%d'%num)
else:
    time.sleep(5)
    num+=1
    print('哈哈2---num=%d'%num)
