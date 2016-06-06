from socket import *

udp = socket(AF_INET,SOCK_DGRAM);

binaddr = ('',2222)

udp.bind(binaddr)

recvdata = udp.recvfrom(1024)

print(recvdata)

udp.close()