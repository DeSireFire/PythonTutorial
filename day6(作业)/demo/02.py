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
			