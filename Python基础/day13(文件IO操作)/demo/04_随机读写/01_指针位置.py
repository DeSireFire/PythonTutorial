path = 'laowang.txt'
file = open(path,'r',encoding='utf-8')

print(file.tell())
file.read(1)
print(file.tell())

file.close()