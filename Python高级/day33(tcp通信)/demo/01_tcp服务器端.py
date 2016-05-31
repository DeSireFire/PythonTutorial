#1.	买个手机
#2.	插上手机卡
#3.	设计手机为正常接听状态（即能够响铃）
#4.	静静的等着别人拨打


from socket import *
# 1.	socket创建一个套接字
tcpServer = socket(AF_INET,SOCK_STREAM)
tcpServer.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
# 2.	bind绑定ip和port
tcpServer.bind(('',5678))
# 3.	listen使套接字变为可以被动链接
tcpServer.listen(5)
# 4.	accept等待客户端的链接
print('服务端监听中......')
#第一个值：关联了服务端和客户端信息，可以与对应的客户端通信
#第二个值：客户端的ip,port
socketClient,cliendAddrdess = tcpServer.accept()

print(socketClient)

tcpServer.close()





