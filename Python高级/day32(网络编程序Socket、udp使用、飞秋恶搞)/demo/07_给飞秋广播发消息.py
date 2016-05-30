from socket import *

#创建socket对象
myUDP = socket(AF_INET,SOCK_DGRAM)
#设置可以向广播地址发消息
myUDP.setsockopt(SOL_SOCKET,SO_BROADCAST,1)
#目的地
destAdress = ('<broadcast>',2425)
#消息内容
sendMsg = input('>>')
#编码
sendMsg = sendMsg.encode('gbk')
#发送
myUDP.sendto(sendMsg,destAdress)

#关闭socket对象
myUDP.close()
print('over......')
