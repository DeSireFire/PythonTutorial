
from socket import *

# 1.socket创建一个套接字
tcpClient = socket(AF_INET,SOCK_STREAM)
# 2.绑定端口号,也可以不绑定
tcpClient.bind(('',8888))
# 3.连接
tcpClient.connect(('192.168.14.72',5678))







