from socket import *
from multiprocessing import *
import os

# 设置静态文件根目录
HTML_ROOT_DIR = "./html"



class MyHttpServer(object):
    """服务器类"""
    def __init__(self):
        """初始化,创建了一个TCP服务端对象"""
        self.server_socket = socket(AF_INET, SOCK_STREAM)

    def bind(self, port=5678):
        """绑定端口号"""
        self.server_socket.bind(("", port))

    def start(self):
        """开始监听"""
        self.server_socket.listen()
        while True:
            client_socket, client_address = self.server_socket.accept()
            print("[%s, %s]用户连接上了" % client_address)
            Process(target=self.handle_client, args=(client_socket,)).start()

    def handle_client(self,client_socket):
        """处理客户端的请求"""
        data = client_socket.recv(1024)
        data = data.decode('utf-8')
        """解析请求报文"""
        # 提取用户请求的文件名,如果是get请求携带参数要处理？
        file_name = data.splitlines()[0].split(' ')[1]

        # 如果是/一般表示请求首页
        if "/" == file_name:
            file_name = "/index.html"

        # 打开文件，读取内容
        try:
            # 模拟一个运行中的异常
            # num=1/0
            with open(HTML_ROOT_DIR + file_name, "rb") as file:
                file_data = file.read()
            # 构造响应数据
            response_start_line = "HTTP/1.1 200 OK" + os.linesep
            response_headers = "Server: My server" + os.linesep
            response_body = file_data.decode("utf-8")
        except FileNotFoundError:
            response_start_line = "HTTP/1.1 404 Not Found" + os.linesep
            response_headers = "Server: My server" + os.linesep
            with open(HTML_ROOT_DIR + '/404.html', "r", encoding='utf-8') as file:
                response_body = file.read()
        except:
            response_start_line = "HTTP/1.1 500 ERROR" + os.linesep
            response_headers = "Server: My server" + os.linesep
            with open(HTML_ROOT_DIR + '/error.html', "r", encoding='utf-8') as file:
                response_body = file.read()

        response_headers += "Content-Type:text/html;charset=utf-8" + os.linesep

        response = response_start_line + response_headers + os.linesep + response_body
        # print("response data:", response)


        client_socket.send(response.encode('utf-8'))
        client_socket.close()



if __name__ == '__main__':
    myHttpServer = MyHttpServer()
    myHttpServer.bind()
    myHttpServer.start()