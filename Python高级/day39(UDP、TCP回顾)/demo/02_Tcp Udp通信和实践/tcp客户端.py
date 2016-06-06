from socket import *

tcpclient = socket(AF_INET,SOCK_STREAM)

tcpclient.bind(("",5555))

tcpclient.connect(("192.168.14.8",5551))