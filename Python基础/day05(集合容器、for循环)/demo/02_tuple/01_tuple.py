'''
	元组：是用小括号的
'''
directions = ('东','西','南','北','中')
print(directions)
print(directions[1])

print('*'*20)

t1 = (1,2,3)
#t1[0]=2

t2 = ([1,2,3],110,'120',(1,2,3))
t2[0].append(110)
print(t2)


'''
	列表和元组相互转换

	ls = list(元组)
	tu = tuple(列表)
'''

ls = [1,2,3]
print(type(ls))
print(ls)

tu = tuple(ls)
print(type(tu))
print(tu)

tu = (1,2,3)
print(type(tu))
print(tu)

ls = list(ls)
print(type(ls))
print(ls)

'''
	变量赋值
'''
a,b = [110,120]
print(a)
print(b)

a,b = (110,120)
print(a)
print(b)
