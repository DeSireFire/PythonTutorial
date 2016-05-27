from threading import *

# global_dict = {}
#
# def std_thread(name):
#     std = name
#     # 把std放到全局变量global_dict中：
#     global_dict[current_thread()] = std
#     do_task_1()
#
# def do_task_1(s):
#     print(global_dict[current_thread()])

#把变量以键值对的形式绑定到当前线程。用处：orm中，可以把session绑定到当前线程
myLocal = local()

def std_thread(name):
    std = name
    myLocal.a = std
    do_task_1()

def do_task_1():
    print(myLocal.a)



if __name__ == '__main__':
    t1 = Thread(target=std_thread,args=('老王',))
    t2 = Thread(target=std_thread, args=('laowang',))

    t1.start()
    t2.start()


    #print(myLocal.a)