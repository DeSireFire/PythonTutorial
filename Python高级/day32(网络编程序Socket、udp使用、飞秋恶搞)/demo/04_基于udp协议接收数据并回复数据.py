from socket import socket,AF_INET,SOCK_STREAM,SOCK_DGRAM

#1. 创建基于UDP协议的socket对象
myUDP = socket(AF_INET,SOCK_DGRAM)
#2. 监听指定的端口号
myUDP.bind(('',8888))
while True:
    #3. 接收数据,地址
    print('等待接收中......')
    recvData,recvAddress = myUDP.recvfrom(1024)
    #4. 回复
    sendData = recvData.decode('gbk')+'--收到了\n'
    myUDP.sendto(sendData.encode('gbk'),recvAddress)
#5. 关闭sockcet
myUDP.close()