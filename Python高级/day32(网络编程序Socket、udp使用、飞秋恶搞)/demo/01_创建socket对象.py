from socket import socket,AF_INET,SOCK_STREAM,SOCK_DGRAM

#创建基于TCP,UDP协议的socket对象
myTCP1 = socket()
myTCP2 = socket(AF_INET,SOCK_STREAM)
myUDP = socket(AF_INET,SOCK_DGRAM)

print(myTCP1)
print(myTCP2)
print(myUDP)


