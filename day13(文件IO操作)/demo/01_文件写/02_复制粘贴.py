'''
	分析:
		1、读
		2、写
'''

pathSrc = input('输入源文件：')
pathDest = input('输入目标文件：')

'''
fileSrc = open(pathSrc,'r',encoding='utf-8')
fileDest = open(pathDest,'w',encoding='utf-8')
'''
fileSrc = open(pathSrc,'rb')
fileDest = open(pathDest,'wb')

content = fileSrc.read()
fileDest.write(content)

fileSrc.close()
fileDest.close()

print('哦啦。。。')