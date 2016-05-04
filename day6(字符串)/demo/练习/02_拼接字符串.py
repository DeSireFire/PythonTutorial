'''
完成一个路径的拼接
先提示用户多次输入路径，最后显示一个完成的路径，比如/home/python/ftp/share

'''
def f(separator):
	ls = []
	while True:
		path = input('输入路径：')
		ls.append(path)
		answer = input('是否继续yes/no：')
		if answer!='yes':
			break
	return '/'+separator.join(ls)

print(f('/'))
			
