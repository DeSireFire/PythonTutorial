from socket import *

#创建套接字
udp = socket(AF_INET,SOCK_DGRAM)

#准备接受地址
address = ('192.168.14.8',8080)

#从键盘获取数据
msg = input("请输入数据:")

#发送到指定电脑
udp.sendto(msg.encode("gbk"),address)

#关闭套接字
udp.close()
