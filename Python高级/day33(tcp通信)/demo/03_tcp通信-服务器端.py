from socket import *

tcpServer = socket(AF_INET,SOCK_STREAM)
tcpServer.bind(('',5678))
tcpServer.listen(5)

print('服务端等待客户端连接......')
socketClient,cliendAddrdess = tcpServer.accept()

data1 = '哈哈。。。。。。'.encode('utf-8')
#给客户端发消息
socketClient.send(data1)
print('发送消息成功......')

#接收客户端发的消息
print('监听中......')
data2 = socketClient.recv(1024)
print(data2)

tcpServer.close()


