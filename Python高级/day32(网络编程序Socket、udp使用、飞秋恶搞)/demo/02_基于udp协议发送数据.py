from socket import socket,AF_INET,SOCK_STREAM,SOCK_DGRAM

#1. 创建基于UDP协议的socket对象
myUDP = socket(AF_INET,SOCK_DGRAM)
#2. 准备接收方的地址
recvAddress = ('192.168.14.58',5678)
#监听指定的端口号,发送方可以不用绑定，但是接收方必须绑定
#myUDP.bind(('',8888))
#3. 准备数据
sendMsg = input('输入要发送的内容：')
#4. 发送数据到指定的电脑上的指定端口号
myUDP.sendto(sendMsg.encode('gbk'),recvAddress)
#5. 关闭套接字
myUDP.close()

print('哦了。。。。。。')