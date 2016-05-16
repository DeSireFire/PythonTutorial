'''
文件的读：
	1、文件在哪？  路径   如果不指定，默认与python解析器的路径一致
			

	2、什么文件？纯文本(解码utf-8,r)，还是非纯文本(二进制字节,rb)

		如果文件不存在，报错
		r,rb   指针从开头开始


	
'''

file = open(r'C:\Users\Administrator\Desktop\老王.txt','r',encoding='utf-8')
print(type(file))
print(file)
print(dir(file))

#content = file.read()
content = file.read(2)
print(content)
file.close()




'''
path = r'C:\Users\Administrator\Desktop\laowang.bmp'
file = open(path,'rb')
content = file.read()
print(content)
file.close()
'''