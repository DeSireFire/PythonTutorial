import os
import time

pid = os.fork()
if pid == 0:
    print('哈哈1')
else:
    time.sleep(5)
    print('哈哈2')

pid = os.fork()
if pid == 0:
    print('哈哈3')
else:
    print('哈哈4')
