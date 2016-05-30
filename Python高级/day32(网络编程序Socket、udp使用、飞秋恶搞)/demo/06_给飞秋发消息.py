from  socket import *

#创建socket对象
myUDP = socket(AF_INET,SOCK_DGRAM)
#目的地
destAdress = ('192.168.14.58',2425)
#消息内容
sendMsg = input('>>')
#编码
sendMsg = sendMsg.encode('gbk')
#发送
myUDP.sendto(sendMsg,destAdress)

#关闭socket对象
myUDP.close()
print('over......')
