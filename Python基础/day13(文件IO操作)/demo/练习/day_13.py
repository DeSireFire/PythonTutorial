
#文件读
path = r"C:\Users\Administrator\Desktop\la.txt"
f = open(path,"rb")
m = f.read()
print("文件读取成功!!!")
f.close()

#文件写入
path = r"C:\Users\Administrator\Desktop\la.txt"
f = open(path,"w",encoding="utf-8")
f.write("老王")
print("文件写入成功!!!")
f.close()

#文件复制
path = r"C:\Users\Administrator\Desktop\07_31.txt"
path1 = r"C:\Users\Administrator\Desktop\la.txt"

f = open(path,"rb")
k = open(path1,"wb")
m = f.read()
k.write(m)
print("文件复制成功!!!")
f.close()
k.close()


path2 = r"C:\Users\Administrator\Desktop\la.txt"
k = open(path2,"a+")
k.write("fhsdkh")
#k.seek(0)
m = k.read()
print("文件后面读取的是:%s"%m)
k.close

print("*****************************************************")

path2 = r"C:\Users\Administrator\Desktop\lala.txt"
k = open(path2,"a+")
k.write("fhsdkh")
k.close

print("*****************************************************")
path2 = r"C:\Users\Administrator\Desktop\la.txt"
l = open(path2,"r")
msg = l.readlines()
print(msg)
l.close

print("*****************************************************")
path2 = r"C:\Users\Administrator\Desktop\la.txt"
l = open(path2,"r")
while l.readline()!='':
	msg = l.readline()
	print(msg)
l.close


print("*****************************************************")
path2 = r"C:\Users\Administrator\Desktop\lala.txt"
l = open(path2,"w")
l.write("laowang")
l.flush()
l.close()

print("*****************************************************")

path2 = r"C:\Users\Administrator\Desktop\lala.txt"
l = open(path2,"r")
print(l.tell())
d = l.read()
print(d)

print(l.tell())
l.close()

import os
print(os.name)
#os.rename(r"C:\Users\Administrator\Desktop\lala.txt",r"C:\Users\Administrator\Desktop\laowang.txt")
print(os.path.sep)
print(os.linesep)#换行符
#os.remove(r"C:\Users\Administrator\Desktop\laowang.txt")

print(os.sep)#  \ windows里面的反斜杠\

import os
print(os.name)
#os.rename(r"C:\Users\Administrator\Desktop\lala.txt",r"C:\Users\Administrator\Desktop\laowang.txt")
print(os.path.sep)
print(os.linesep)#换行符
#os.remove(r"C:\Users\Administrator\Desktop\laowang.txt")

print(os.sep)#  \ windows里面的反斜杠\

print(os.path.basename(r"C:\Users\Administrator\Desktop"))#获取文件地址
print(os.path.dirname(r"C:\Users\Administrator\Desktop"))#获取文件路径
print(os.path.getsize(r"C:\Users\Administrator\Desktop"))#获取大小

print(os.getcwd())#获取文件路径
#os.mkdir(r"C:\Users\Administrator\Desktop\老王")

#os.makedirs(r"C:\Users\Administrator\Desktop\老\lao\wang\ji")

#os.rmdir(r"C:\Users\Administrator\Desktop\老王")

import shutil
#shutil.rmtree(r"C:\Users\Administrator\Desktop\老")

import os.path
#print(os.path.join(m,n))

def copya():
	#提示用户输入复制文件名称和目标文件名称
	source = input("请输入源文件名称:")
	target = input("请输入目标文件名称:")
	#打开文件
	old_file = open(source,"br")
	new_file = open(target,"bw")

	#开始复制
	while True:
		content = old_file.read(1024*1024)
		if content:
			new_file.write(content)
		else:
			print("文件复制完成!!!")
			break
	old_file.close()
	new_file.close()	
copya()

'''
#C:\Users\Administrator\Desktop
#备份文件
def bak_file():
	file_name = input("请输入您要备份的文件名称:")
	#获取文件名称
	sep = file_name.rindex("/")
	dir = file_name[:sep+1]
	name = file_name[sep+1:]
	#拆分文件名称，拼接成新的文件名称
	new_file_name =dir + "[备份]" + name
	#开始读写文件
	old_file = open(file_name,"br")
	bak_file = open(new_file_name,"bw")
	while True:
		content = old_file.read(1024*1024)
		if content:
			bak_file.write(content)
		else:
			print("文件备份完成!!!")
			break
	old_file.close()
	bak_file.close()	
bak_file()	
'''
path = input("请输入文件的路径:").strip()
list = os.listdir(path)
print(list)
for n in list:
	#拼接路径
	old_path = os.path.join(path,n)
	if os.path.isfile(old_path):
		index = n.rfind(".")
		new_name = n[:index]+"-lalal"+n[index:]
	else:
		new_name = n+"-lalal"
	new_path = os.path.join(path,new_name)
	os.rename(old_path,new_path)
#print(list)
print("修改完成!!!")