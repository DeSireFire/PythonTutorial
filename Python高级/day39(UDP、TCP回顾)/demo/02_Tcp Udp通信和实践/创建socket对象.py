from socket import *

tcp1 = socket()
tcp2 = socket(AF_INET,SOCK_STREAM)
ucp1 = socket(AF_INET,SOCK_DGRAM)

print(tcp1)
print(tcp2)
print(ucp1)