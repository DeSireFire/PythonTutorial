from socket import socket,AF_INET,SOCK_STREAM,SOCK_DGRAM

#1. 创建基于UDP协议的socket对象
myUDP = socket(AF_INET,SOCK_DGRAM)
#2. 监听指定的端口号
myUDP.bind(('',8888))
#3. 接收数据,如果接收不到，阻塞。接收到之后，
# 返回一个元组（数据字节,(发送放的ip,port)）
print('等待接收中......')
recvData = myUDP.recvfrom(1024)
#4. 处理数据
msg = recvData[0].decode('gbk')
ip = recvData[1][0]
port = recvData[1][1]

myMsg = '【Receive from %s : %s】：%s'%(ip,port,msg)
print(myMsg)
#5. 关闭sockcet
myUDP.close()