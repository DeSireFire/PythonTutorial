from socket import *

udp = socket(AF_INET,SOCK_DGRAM)

addr = ("192.168.14.8",4567)

msg = input("please input msg:")

udp.sendto(msg.encode("gbk"),addr)

udp.close()

print("OK")