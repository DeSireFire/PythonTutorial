import socket
from signal import signal,SIGCHLD,pause
from multiprocessing import Process,active_children
from os import linesep
# from threading import Thread

filePath = "./天天生鲜"
class MyHTTP(object):
    def __init__(self):
        self.myServer = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    def bind(self,port):
        self.myServer.bind(("",port))
        self.myServer.listen(128)

    def start(self):
        signal(SIGCHLD,self.__recycle)
        # Thread(target=self.__monitoring).start()
        # self.__monitoring()
        while True:
            clientSocket,clientAddress = self.myServer.accept()
            Process(target=self.clientHandler,args=(clientSocket,clientAddress)).start()
            clientSocket.close()

    def clientHandler(self,clientSocket,clientAddress):
        recvData = clientSocket.recv(1024).decode("utf-8")

        recvData = recvData.splitlines()
        fileName = recvData[0].split(" ")[1].split("?",1)
        if fileName == "/":
            fileName = "/loginPage.html"
        print("加载：%s"%fileName)

        try:
            with open(filePath+fileName,"rb") as f:
               fileData = f.read()
            responseStart = recvData[0].split(" ")[2] + " 200 OK" + linesep
            responseHeader = "myServer:laowang" + linesep
        except FileNotFoundError:
            responseStart = recvData[0].split(" ")[2] + " 404 NotFound" + linesep
            responseHeader = "myServer:laowang" + linesep
            fileData = b""

        response = responseStart + responseHeader + linesep
        clientSocket.send(response.encode("utf-8"))  #string
        clientSocket.send(fileData)  #byte
        clientSocket.close()

    def __recycle(self,*args):# recycle 回收
        active_children()

    # def __monitoring(self):
    #     while True:
    #        pause()
    #        print("haha")
    #        active_children()

if __name__ == "__main__":
    myServer = MyHTTP()
    myServer.bind(8080)
    myServer.start()