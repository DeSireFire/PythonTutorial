from socket import *

tcpclient = socket(AF_INET,SOCK_STREAM)

addr = ("192.168.14.8",5678)
tcpclient.connect(addr)

sendData = input("input:")
tcpclient.send(sendData.encode("gbk"))

recvData = tcpclient.recv(1024)
print("received:%s"%recvData.decode("gbk"))

tcpclient.close()