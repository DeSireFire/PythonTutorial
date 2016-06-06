from socket import *
from threading import Thread
from time import ctime

udp1 = socket(AF_INET,SOCK_DGRAM)
binaddr = ('',7720)
udp1.bind(binaddr)

class myThread(Thread):
    def __init__(self,udp,data,address):
        Thread.__init__(self)
        self.data = data
        self.udp = udp
        self.address = address

    def run(self):
        sendData = ctime()+self.data + "-------收到\n"
        self.udp.sendto(sendData.encode("gbk"),self.address)


while True:

    print("等待接收数据")
    recvdata = udp1.recvfrom(1024)
    msgg1 = recvdata[1]
    msgg = recvdata[0].decode("gbk")
    myThread(udp1,msgg,msgg1).start()

udp1.close()