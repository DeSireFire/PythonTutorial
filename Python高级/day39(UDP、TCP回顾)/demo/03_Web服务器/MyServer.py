'这是自定义的服务器模块'

import socket
import multiprocessing
import os
import time
import re
import sys


class MyHttpServer(object):

    def __init__(self,application):
        serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.serverSocket = serverSocket
        self.application = application

    def bind(self, port=8000):
        self.serverSocket.bind(('', port))

    def start(self):
        self.serverSocket.listen()
        while True:
            # 接收
            clientSocket, clientAddr = self.serverSocket.accept()
            print(clientSocket)
            # 开一个新的进程，执行交互
            multiprocessing.Process(target=self.clientHandler, args=(clientSocket, clientAddr)).start()
            # 关闭客户端对象
            clientSocket.close()

    def clientHandler(self, clientSocket, clientAddr):
            #请求信息，字符串
            recvData = clientSocket.recv(1024).decode('utf-8')
            #获取用户的请求的地址
            fileName = re.split(r' +', recvData.splitlines()[0])[1]
            #获取用户的请求方式GET or POST
            method = re.split(r' +', recvData.splitlines()[0])[0]
            env = {
                'PATH_INFO': fileName,
                'METHOD':method
            }
            for item in recvData:
                if item.count(':')!=0:
                    k,v = item.split(':')
                    env[k] = v
            responseBody = self.application(env,self.startResponse)

            sendData = (self.responseHeader + os.linesep + os.linesep + responseBody).encode('utf-8')
            clientSocket.send(sendData)
            clientSocket.close()

    def startResponse(self, status, responseHeaders):
        self.responseHeader = status+os.linesep
        for k, v in responseHeaders:
            kv = (k + ':' + v + os.linesep)
            self.responseHeader += kv

def main():
    print(sys.argv)
    moduleName, attrName = sys.argv[1].split(':')
    myModule = __import__(moduleName)
    server = MyHttpServer(getattr(myModule,attrName))
    server.bind(8000)
    server.start()

if __name__ == '__main__':
    main()
