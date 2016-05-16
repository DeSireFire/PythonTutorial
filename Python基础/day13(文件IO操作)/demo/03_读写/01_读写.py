'''
	写
	需要注意访问模式。到底是操作的是字节还是字符
'''

'''
path = 'laowang.txt'
file = open(path,'wb')
message = '老王，该上课啦。'
file.write(message.encode('utf-8'))
file.close()
'''


'''
读

read:读所有的内容，并返回
readlines：读所有的内容，按照换行符分割，返回列表
readline：读一行
'''


'''
path = 'laowang.txt'
file = open(path,'r',encoding='utf-8')
content = file.read()
print(content)
file.close()



path = 'laowang.txt'
file = open(path,'r',encoding='utf-8')
content = file.readlines()
print(content)
file.close()


path = 'laowang.txt'
file = open(path,'r',encoding='utf-8')
content = file.readline()
print(content)
content = file.readline()
print(content)
file.close()
'''

path = '老王.jpg'
file = open(path,'rb')

content = file.readline()
while content!=b'':
	print(content)
	content = file.readline()
file.close()