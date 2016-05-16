'''
	可以读写字符，需要指定编码格式

	1、r	从开头读
	2、w	从开头写
	3、a	从末尾写   续写   


	可以读写字节，不需要指定编码格式

	1、r+	从开头读（写）
	2、w+	从开头写（读）
	3、a+	从末尾写（读）   续写 



	可以读写字节，不需要指定编码格式

	1、rb	从开头读
	2、wb	从开头写
	3、ab	从末尾写   续写 


	可以读写字节，不需要指定编码格式

	1、rb+	从开头读(写)
	2、wb+	从开头写（读）
	3、ab+	从末尾写(读)   续写 
	

	
		

'''

file1 = open(r'C:\Users\Administrator\Desktop\laowang.txt','r',encoding='utf-8')
content = file1.read(2)
file1.close()
print(content)

print('************************************华丽的分割线************************************')

file2 = open(r'C:\Users\Administrator\Desktop\laowang1.txt','w',encoding='utf-8')
content = file2.write('999')
file2.close()

print('************************************华丽的分割线************************************')

file3 = open(r'C:\Users\Administrator\Desktop\laowang2.txt','a',encoding='utf-8')
content = file3.write('老王')
file3.close()


print('************************************华丽的分割线************************************')

file3 = open(r'C:\Users\Administrator\Desktop\laowang3.txt','w+',encoding='utf-8')
content = file3.read()
file3.close()


print('************************************华丽的分割线************************************')

file3 = open(r'C:\Users\Administrator\Desktop\laowang4.txt','w+',encoding='utf-8')
content = file3.write('老王')
content = file3.write('laowang')
file3.close()


print('************************************华丽的分割线************************************')

file3 = open(r'C:\Users\Administrator\Desktop\laowang5.txt','r+',encoding='gbk')
content = file3.read(1)
print(content)
content = file3.read(1)
print(content)
file3.close()
