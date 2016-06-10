import threading

local = threading.local()

def haha():
    std = local.a
    print("nihao%s,in%s"%(std,threading.current_thread().name))

def lala(name):
    local.a = name
    haha()


a = threading.Thread(target=lala,args=("laowang",),name="A")
b = threading.Thread(target=lala,args=("laoli",),name="B")
a.start()
b.start()

a.join()
b.join()