from socket import *
from multiprocessing import *
import os


def handleClient(clientSocket):
    data = clientSocket.recv(1024).decode('utf-8')
    print(data)

    responseHeaderLines = "HTTP/1.1 200 OK"+os.linesep
    responseHeaderLines += "k1:v1"+os.linesep
    responseHeaderLines += "k2:v2" + os.linesep
    responseHeaderLines += os.linesep
    responseBody = "hello <h1>老王八</h1>"
    response = responseHeaderLines + responseBody

    clientSocket.send(response.encode('utf-8'))
    clientSocket.close()


if __name__ == '__main__':
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind(("", 82))
    serverSocket.listen()
    while True:
        print('服务端等待客户端连接......')
        clientSocket, clientAddr = serverSocket.accept()
        Process(target=handleClient, args=(clientSocket,)).start()
        print('%s-%s 连接成功......' % (clientAddr[0], clientAddr[1]))
