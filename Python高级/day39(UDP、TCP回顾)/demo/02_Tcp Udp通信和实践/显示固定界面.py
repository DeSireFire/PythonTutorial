from socket import *
from multiprocessing import *
import os

def lala(msg):
    data1 = msg.recv(1024).decode("gbk")
    print(data1)

    a = "HTTP/1.0 200 OK"+os.linesep
    a += "k1:v1"+os.linesep
    a += "k2:v2"+os.linesep
    a += os.linesep
    b = "Hello <h2>老王</h2>"
    rs = a + b
    msg.send(rs.encode("gbk"))
    msg.close()

if __name__ == '__main__':

    tcpserver = socket(AF_INET,SOCK_STREAM)

    tcpserver.bind(("",8223))

    tcpserver.listen()

    while True:
        print("等待客户端链接")
        data,addr = tcpserver.accept()
        Process(target=lala,args=(data,)).start()
        print("%s,%s链接成功"%(addr[0],addr[1]))