from socket import *
from threading import *


class MyThread(Thread):
    def __init__(self,socketClient,cliendAddrdess):
        self.socketClient = socketClient
        self.cliendAddrdess = cliendAddrdess
        Thread.__init__(self)

    def run(self):
        data1 = '哈哈。。。。。。可以聊天了'.encode('utf-8')
        self.socketClient.send(data1)

        while True:
            try:
                # 接收客户端发的消息
                data = self.socketClient.recv(1024).decode('utf-8')
            except:
                print('<<\t%s-%s 已经断开了' % (self.cliendAddrdess[0], self.cliendAddrdess[1]))
                break
            if data=='886':
                break
            print('<<\t%s-%s:%s'%(self.cliendAddrdess[0],self.cliendAddrdess[1],data))



if __name__ == '__main__':
    tcpServer = socket(AF_INET,SOCK_STREAM)
    tcpServer.bind(('',5678))
    tcpServer.listen(5)


    while True:
        print('服务端等待客户端连接......')
        socketClient,cliendAddrdess = tcpServer.accept()
        MyThread(socketClient,cliendAddrdess).start()
        print('%s-%s 连接成功......'%(cliendAddrdess[0],cliendAddrdess[1]))

#tcpServer.close()


