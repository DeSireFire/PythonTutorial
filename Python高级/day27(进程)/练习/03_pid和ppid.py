import os,time

pid = os.fork()

if pid == 0:
    print('哈哈1:pid=%s,ppid=%s'%(os.getpid(),os.getppid()))
else:
    print('哈哈2:pid=%s,ppid=%s' % (os.getpid(), os.getppid()))
