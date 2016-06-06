from socket import *
from multiprocessing import *
import os

# 设置静态文件根目录
HTML_ROOT_DIR = "./html"


def handleClient(clientSocket):
    data = clientSocket.recv(1024)
    data = data.decode('utf-8')
    """解析请求报文"""
    # 提取用户请求的文件名,如果是get请求携带参数要处理？
    file_name = data.splitlines()[0].split(' ')[1]

    #如果是/一般表示请求首页
    if "/" == file_name:
        file_name = "/index.html"

    # 打开文件，读取内容
    try:
        #模拟一个运行中的异常
        #num=1/0
        with open(HTML_ROOT_DIR + file_name, "rb") as file:
            file_data = file.read()
        # 构造响应数据
        response_start_line = "HTTP/1.1 200 OK"+os.linesep
        response_headers = "Server: My server"+os.linesep
        response_body = file_data.decode("utf-8")
    except FileNotFoundError:
        response_start_line = "HTTP/1.1 404 Not Found"+os.linesep
        response_headers = "Server: My server"+os.linesep
        with open(HTML_ROOT_DIR + '/404.html', "r",encoding='utf-8') as file:
            response_body = file.read()
    except:
        response_start_line = "HTTP/1.1 500 ERROR" + os.linesep
        response_headers = "Server: My server" + os.linesep
        with open(HTML_ROOT_DIR + '/error.html', "r",encoding='utf-8') as file:
            response_body = file.read()

    response_headers += "Content-Type:text/html;charset=utf-8" + os.linesep

    response = response_start_line + response_headers + os.linesep + response_body
    #print("response data:", response)


    clientSocket.send(response.encode('utf-8'))
    clientSocket.close()


if __name__ == '__main__':
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind(("", 6788))
    serverSocket.listen()
    while True:
        print('服务端等待客户端连接......')
        clientSocket, clientAddr = serverSocket.accept()
        Process(target=handleClient, args=(clientSocket,)).start()
        print('%s-%s 连接成功......' % (clientAddr[0], clientAddr[1]))
