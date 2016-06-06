from socket import *

tcpclient = socket(AF_INET,SOCK_STREAM)

tcpclient.bind(("",8888))

tcpclient.connect(("192.168.14.8",5555))

while True:
    msg = input(">>>").encode("gbk")
    tcpclient.send(msg)
    if msg == "886":
        tcpclient.close()
        break