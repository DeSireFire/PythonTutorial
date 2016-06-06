from socket import *
import threading

class MyT(threading.Thread):
    def __init__(self,udp,data,addr):
        self.udp = udp
        self.data = data
        self.addr = addr
        threading.Thread.__init__(self)

    def run(self):
        msg = self.data.decode("gbk")+"收到啦"
        self.udp.sendto(msg.encode("gbk"),self.addr)

if __name__ == '__main__':

    udp = socket(AF_INET,SOCK_DGRAM)
    udp.bind(("",5556))

    while True:
        print("等待接收数据")
        data,addr = udp.recvfrom(1024)
        print(data.decode("gbk"))
        MyT(udp,data,addr).start()

    udp.close()