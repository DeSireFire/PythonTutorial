from socket import *

tcpserver = socket(AF_INET,SOCK_STREAM)

add = ("",4566)
tcpserver.bind(add)

tcpserver.listen(5)

newSocket,clientAddr = tcpserver.accept()

revData = newSocket.recv(1024)

print("Ip:%s"%clientAddr[0])
print("Prot:%s"%clientAddr[1])
print("Data:%s"%revData.decode("gbk"))

newSocket.send(("Thank You 老王\n").encode("gbk"))

newSocket.close()
tcpserver.close()