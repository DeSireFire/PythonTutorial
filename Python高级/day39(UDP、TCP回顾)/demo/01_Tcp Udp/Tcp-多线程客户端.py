from socket import *
from time import *

# 1.socket创建一个套接字
tcpClient = socket(AF_INET,SOCK_STREAM)
# 2.绑定端口号,也可以不绑定
tcpClient.bind(('',7788))
# 3.连接
tcpClient.connect(('192.168.14.85',7788))
#4.接收消息
# data1 = tcpClient.recv(1024)
# print(data1.decode('utf-8'))

#5.发消息
while True:
    data = input('>>\t').encode('utf-8')
    tcpClient.send(data)
    if data=='886':
        sleep(4)
        tcpClient.close()
        break
