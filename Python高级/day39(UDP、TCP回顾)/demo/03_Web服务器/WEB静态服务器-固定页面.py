import socket
from multiprocessing import Process

def handleClient(clientSocket):
    #用一个新的进程，为一个客户端进行服务
    recvData = clientSocket.recv(1024)
    requestHanderLines = recvData.splitlines()
    for i in requestHanderLines:
        print(i.decode("utf-8"))

    responseHeaderLines = "HTTP/1.1 200 OK\r\n"
    responseHeaderLines += "Server:laowang\r\n"
    responseHeaderLines += "\r\n"
    responseBody = "hello world"

    response = responseHeaderLines + responseBody
    clientSocket.send(bytes(response, 'gbk'))
    clientSocket.close()

def main():
    serverSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    serverSocket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    addr = ("",5568)
    serverSocket.bind(addr)
    serverSocket.listen(5)
    while True:
        clientSocket,clientAddr = serverSocket.accept()
        clientP = Process(target=handleClient,args=(clientSocket,))
        clientP.start()
        clientSocket.close()

if __name__ == '__main__':
    main()