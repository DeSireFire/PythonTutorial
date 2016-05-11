import os
import os.path

path = input('输入路径:')
#列出所有文件和文件夹
ls = os.listdir(path)
print(ls)

#遍历
for file in ls:
	#拼接路径
	oldPath = os.path.join(path,file)
	#判断是否是文件
	if os.path.isfile(oldPath):
		index = file.rfind('.')
		newName = file[0:index]+'-new'+file[index:]
	else:
		newName = file+'-new'
	
	newPath = os.path.join(path,newName)
	#重命名
	os.rename(oldPath,newPath)

print('哦啦。。。')