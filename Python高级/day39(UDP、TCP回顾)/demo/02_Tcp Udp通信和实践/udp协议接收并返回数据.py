from socket import *

udp = socket(AF_INET,SOCK_DGRAM)

udp.bind(("",5555))

while True:

    data,addr = udp.recvfrom(1024)

    print(data.decode("gbk"))

    msg = data.decode("gbk")+"收到"

    udp.sendto(msg.encode("gbk"),addr)

udp.close()

