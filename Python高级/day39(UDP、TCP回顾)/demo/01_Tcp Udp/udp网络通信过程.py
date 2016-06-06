from socket import *

udp = socket(AF_INET,SOCK_DGRAM)

bindadd = ("",33991)

udp.bind(bindadd)

num = 1
while True:

    revmsg = udp.recvfrom(1024)

    udp.sendto(revmsg[0],revmsg[1])

    msg = revmsg[0]

    print("内容:%s"%(msg.decode("gbk")))

    num+=1

udp.close()