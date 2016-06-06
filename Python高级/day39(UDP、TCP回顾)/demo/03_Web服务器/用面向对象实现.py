from socket import *
from multiprocessing import *
import os

#设置静态文件目录
HTML_ROOT_DIR = "./html"

class MyHttpServer():
    """服务器类"""
    def __init__(self):
        """初始化，创建一个Tcp服务端对象"""
        self.server_socket = socket(AF_INET,SOCK_STREAM)

    def bind(self,prot=5678):
        self.server_socket.bind(("",prot))

    def start(self):
        """开始监听"""
        self.server_socket.listen()
        while True:
            client_socket,client_address = self.server_socket.accept()
            print("[%s,%s]用户连接上了"%(client_address[0],client_address[1]))
            Process(target=self.handle_client,args=(client_socket,)).start()

    def handle_client(self,client_socket):
        """处理客户端的请求"""
        data = client_socket.recv(1024).decode("utf-8")
        """解析请求报文"""
        file_name = data.splitlines()[0].split(" ")[1]

        #如果是/表示一般请求首页
        if "/"==file_name:
            file_name = "./index.html"
        #打开文件，读取内容
        try:
            with open(HTML_ROOT_DIR + file_name,"rb") as file:
                file_data = file.read()
            #构造响应数据
            s_l = "HTTP/1.1 200 OK"+os.linesep
            h = "Server: My server" + os.linesep
            b = file_data.decode("utf-8")

        except FileNotFoundError:
            s_l = "HTTP/1.1 404 Not Found" + os.linesep
            h = "Server: My server" + os.linesep
            with open(HCI_DATA_DIR + "/404.html","r",encoding="utf-8") as f:
                b = f.read()
        except:
            s_l = "HTTP/1.1 500 Not Found" + os.linesep
            h = "Server: My server" + os.linesep
            with open(HCI_DATA_DIR + "/error.html", "r", encoding="utf-8") as f:
                b = f.read()

        h += "Content-Type:text/html;charset=utf-8"+os.linesep
        res = s_l + h + os.linesep + b

        client_socket.send(res.encode("utf-8"))
        client_socket.close()


if __name__ == '__main__':
    m_H_S = MyHttpServer()
    m_H_S.bind()
    m_H_S.start()