from socket import *
import threading

class myT(threading.Thread):
    def __init__(self,data,addr):
        self.data = data
        self.addr = addr
        threading.Thread.__init__(self)
    def run(self):
        data1 = "可以聊天啦".encode("gbk")
        self.data.send(data1)

        while True:
            try:
                data2 = self.data.recv(1024).decode("gbk")
            except:
                print("已经断开").encode("utf-8")
                break
            if data2=="886":
                break
            print(data2)

if __name__ == '__main__':

    tcpserver = socket(AF_INET,SOCK_STREAM)
    tcpserver.bind(("",5555))
    tcpserver.listen(5)

    while True:
        print("等待客户端链接")
        data,addr = tcpserver.accept()
        myT(data,addr).start()
        print("哈哈，连接上啦")
