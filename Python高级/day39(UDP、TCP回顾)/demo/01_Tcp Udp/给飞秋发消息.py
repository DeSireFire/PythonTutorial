from socket import *

#创建套接字
udp = socket(AF_INET,SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST,1)

address = ('<broadcast>',2425)

#从键盘获取数据
msg = input("请输入数据:")
# 版本号: 包编号:发送者姓名: 发送者机器名:命令字: 消息
# 1: 12323434:user: machine:32: hello

#发送到指定电脑
udp.sendto(msg.encode("gbk"),address)
print("over")
#关闭套接字1:12323434:user:machine:32:hello
udp.close()

