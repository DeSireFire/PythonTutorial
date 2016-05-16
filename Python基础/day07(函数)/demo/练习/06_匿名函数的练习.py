# 匿名函数的练习
f1 = lambda a,b:a*b
print(f1(2,3))

f2 = lambda ls:ls.append(119)
ls = [110,120,111]
f2(ls)
print(ls)
print(f2(ls))

def ll(func):
	ret = func(2,6)
	print(ret)

def ha(a,b):
	return a*b
ll(ha)
k = lambda a,b:a*b
print(k(5,9))

ka = 'fjkdshkfj'
print(ka[:])
print(ka[:5])
print(ka[1:5])
print('&&&&&&&')
print(ka[:-1])
print(ka[-1:])
print('&&&&&&&')
print(ka[1:-1])
print(ka[:-4])
