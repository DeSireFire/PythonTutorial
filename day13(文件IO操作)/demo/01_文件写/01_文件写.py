'''
文件的写：
	1、文件在哪？  路径  如果不指定，默认与python解析器的路径一致
		

	2、什么文件？纯文本(解码utf-8,w)，还是非纯文本(二进制字节,wb)
		如果文件不存在，新建

		w,wb   指针从开头开始

		如果文件不存在，新建。
		如果文件存在，清空原来的内容，再写入新的内容
'''

import time

path = r'laowang.txt'
file = open(path,'w',encoding='utf-8')
file.write('laowang')
file.close()

