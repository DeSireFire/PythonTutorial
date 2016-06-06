from socket import *
import threading

def rev():
    while True:
        info = udp.recvfrom(1024)
        print("接收到:%s,地址%s"%(info[0].decode("gbk"),info[1]))

def send():
    while True:
        ms = input()
        udp.sendto(ms.encode("gbk"),(ip,port))

udp = None
ip = "192.168.14.8"
port = 4567

if __name__ == '__main__':

    udp = socket(AF_INET,SOCK_DGRAM)

    udp.bind(("",5560))

    t1 = threading.Thread(target=rev)
    t2 = threading.Thread(target=send)

    t1.start()
    t2.start()