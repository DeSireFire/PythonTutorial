from threading import Thread
from socket import *

def recvData():
    while True:
        recvInfo = udp.recvform(1024)
        print("%s:%s"%(str(recvInfo[1]),recvInfo[0]))

def sendData():
    while True:
        sendInfo = input("===>")
        udp.sendto(sendInfo.encode("gb2312"),(Ip,port))

udp = None
Ip = ""
port = 0

def main():
    global udp
    global Ip
    global port

    Ip = input("对方的IP：")
    port = input("对发端口:")

    udp = socket(AF_INET,SOCK_DGRAM)
    udp.bind("",4567)

    t1 = Thread(target=recvData())
    t2 = Thread(target=sendData())

    t1.start()
    t2.start()

    t1.join()
    t2.join()