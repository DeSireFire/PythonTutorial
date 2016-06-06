from socket import *

udp = socket(AF_INET,SOCK_DGRAM)

address = ('192.168.14.8',8080)

msg = input("请输入数据:")

udp.sendto(msg.encode("gbk"),address)

#等待接收对方发送的数据
revdata = udp.recvfrom(1024)

print(revdata)

msga = revdata[0]
ip = revdata[1][0]
forp = revdata[1][1]

print("IP:%s,端口号:%s,内容:%s"%(ip,forp,msga.decode("gbk")))

udp.close()