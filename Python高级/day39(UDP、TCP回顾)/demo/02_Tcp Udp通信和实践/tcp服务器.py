from socket import *

tcpserver = socket(AF_INET,SOCK_STREAM)

tcpserver.bind(("",5551))

tcpserver.listen(5)

dat,ip = tcpserver.accept()

print(dat,ip)

tcpserver.close()
#<socket.socket fd=4, family=AddressFamily.AF_INET,
# type=SocketKind.SOCK_STREAM, proto=0, laddr=('192.168.14.85', 5551),
# raddr=('192.168.14.8', 52273)> ('192.168.14.8', 52273)
