import socket,os,threading

html_root = "./"

class myP(threading.Thread):
    def __init__(self,data):
        self.data = data
        threading.Thread.__init__(self)
    def run(self):
        data1 = self.data.recv(1024)
        data2 = data1.decode("utf-8")

        file_name = data2.splitlines()[0].split(" ")[1]

        if "/" == file_name:
            file_name = "/a.html"

        try:
            with open(html_root + file_name,"rb") as f:
                file_data = f.read()
            a = "HTTP/1.1 200 OK"+os.linesep
            h = "charles:long"+os.linesep
            b = file_data.decode("utf-8")
        except FileNotFoundError:
            a = "HTTP/1.1 404 Not Found" + os.linesep
            h = "charles:long" + os.linesep
            with open(html_root + "/b.html","r",encoding="utf-8")as f:
                b = f.read()
        except:
            a = "HTTP/1.1 500 Error" + os.linesep
            h = "charles:long" + os.linesep
            with open(html_root + "/c.html","r",encoding="utf-8")as f:
                b = f.read()
        h += "Content-Type:text/html;charset=utf-8" + os.linesep
        response = a + h + os.linesep + b

        self.data.send(response.encode("utf-8"))
        self.data.close()


if __name__ == '__main__':
    tcpserver = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    tcpserver.bind(("",5694))
    tcpserver.listen(10)
    while True:
        print("等待链接!!!")
        data,addr = tcpserver.accept()
        myP(data).start()
        print("%s----%s链接成功"%(addr[0],addr[1]))