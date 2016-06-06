from socket import *

tcpserver = socket(AF_INET,SOCK_STREAM)

tcpserver.bind(("",5555))

tcpserver.listen(5)

print("等待客户端链接")
data,addr = tcpserver.accept()

msg = "哈哈，连接上啦".encode("gbk")
data.send(msg)
print("消息发送sucess")

print("监听中")
dataa = data.recv(1024)
print(dataa.decode("gbk"))

tcpserver.close()

