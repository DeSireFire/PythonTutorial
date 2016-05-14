import gc

class ClassA():
    def __init__(self):
        print('object born,id:%s'%str(hex(id(self))))

def f2():
    while True:
        c1 = ClassA()
        c2 = ClassA()
        c1.t = c2
        c2.t = c1
        del c1
        del c2

#把python的gc关闭
#gc.disable()

f2()


'''
gc垃圾回收机制，自动回收垃圾对象。不需要程序员手动写代码控制。
两种方式：
	1、标记清除法
	2、隔代回收法
'''
