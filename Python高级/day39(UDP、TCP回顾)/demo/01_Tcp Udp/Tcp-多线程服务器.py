from socket import *
from threading import *

class MyThread(Thread):
    def __init__(self,newSocket,clientAddr):
        self.newSocket = newSocket
        self.clientAddr = clientAddr
        Thread.__init__(self)


    def run(self):
        data1 = '哈哈。。。。。。可以聊天了'.encode('utf-8')
        self.newSocket.send(data1)

        while True:
            try:
                # 接收客户端发的消息
                recvData = self.newSocket.recv(1024).decode("utf-8")
            except:
                print('<<\t%s-%s 已经断开了' % (self.cliendAddrdess[0], self.cliendAddrdess[1]))
                break
            if (recvData=='886'):
                break

if __name__ == '__main__':

    tcpServer = socket(AF_INET, SOCK_STREAM)
    add = ("", 7789)
    tcpServer.bind(add)
    tcpServer.listen(5)

    while True:
        print('服务端等待客户端连接......')
        newSocket,clientAddr = tcpServer.accept()
        #print(tcpServer.accept())
        MyThread(newSocket,clientAddr).start()
        print('%s-%s 连接成功......' % (clientAddr[0], clientAddr[1]))


# tcpServer.close()