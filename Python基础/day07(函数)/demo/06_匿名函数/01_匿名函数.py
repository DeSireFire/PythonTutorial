'''
lambda
有的函数功能简单，只用一次，可以使用lambda表达式简写
'''

def haha(a,b):
	return a+b

f1 = lambda a,b:a+b

print(f1)
print(f1(1,2))


f2 = lambda ls:ls.append(110)
ls = [1,2,3]
f2(ls)
print(ls)
print(f2(ls))


def outer(func):
	ret = func(1,2)
	print(ret)

def haha(a,b):
	return a+b

outer(haha)

outer(lambda a,b:a+b)