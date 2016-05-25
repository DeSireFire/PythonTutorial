import os,time

pid = os.fork()

if pid == 0:
    time.sleep(1)
    print('哈哈1')
else:
    time.sleep(10)
    print('哈哈2')





# print('hello 老王')
#
# time.sleep(100000)
