from socket import socket,AF_INET,SOCK_STREAM,SOCK_DGRAM
from threading import Thread
from time import sleep

class MyThread(Thread):
    def __init__(self,udpSocket,recvData,recvAddress):
        self.recvData = recvData
        self.recvAddress = recvAddress
        self.udpSocket = udpSocket
        Thread.__init__(self)

    def run(self):
        sendData = self.recvData.decode('gbk') + '--收到了\n'
        self.udpSocket.sendto(sendData.encode('gbk'),self.recvAddress)



#1. 创建基于UDP协议的socket对象
myUDP = socket(AF_INET,SOCK_DGRAM)
#2. 监听指定的端口号
myUDP.bind(('',8888))
while True:
    #3. 接收数据,地址
    print('等待接收中......')
    recvData,recvAddress = myUDP.recvfrom(1024)
    #4. 回复
    MyThread(myUDP,recvData,recvAddress).start()

#5. 关闭sockcet
myUDP.close()