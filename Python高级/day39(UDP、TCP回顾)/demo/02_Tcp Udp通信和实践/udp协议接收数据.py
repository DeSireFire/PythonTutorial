from socket import *

udp = socket(AF_INET,SOCK_DGRAM)

udp.bind(("",5555))

print("等待接收")
msg = udp.recvfrom(1024)

print(msg)

data = msg[0].decode("gbk")
ip = msg[1][0]
port = msg[1][1]

print("data=%s,ip=%s,port=%s"%(data,ip,port))