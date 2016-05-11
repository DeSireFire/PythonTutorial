
pathSrc = input('输入源文件：')
pathDest = input('输入目标文件：')

fileSrc = open(pathSrc,'rb')
fileDest = open(pathDest,'wb')

content = fileSrc.read()
fileDest.write(content)



content = fileSrc.readline()
while content!=b'':
	fileDest.write(content)
	fileDest.flush()
	content = file.readline()

fileSrc.close()
fileDest.close()

print('哦啦。。。')