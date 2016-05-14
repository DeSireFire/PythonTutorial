'''
	内置函数，python解析器在启动的时候，已经加载好了
	可以直接调用
	不要后期覆盖
'''
print(dir(__builtins__))

print('******************************华丽的分割线******************************')

for i in range(0,10,2):
	print(i)

print('******************************华丽的分割线******************************')

ls = [1,2,3]


def f(num):
	return num**2


ls2 = list(map(f,ls))

print(ls2)


ret = map(lambda x:x**2,ls)
print(list(ret))



ret = map(lambda x, y: x+y, [1, 2, 3], [4, 5, 6])
print(list(ret))


def f1( x, y ):  
    return (x,y)

l1 = [ 0, 1, 2, 3, 4, 5, 6 ]  
l2 = [ 'Sun', 'M', 'T', 'W', 'T', 'F', 'S' ]
#l3 = map( f1, l1, l2 ) 
l3 = map(lambda x,y:(x,y), l1, l2 ) 
print(list(l3))


print('******************************华丽的分割线******************************')
'''
if里条件相当于False

False
0
None
''
'''


ret = filter(lambda x: x%2, [1, 2, 3, 4])
print(list(ret))

import os

'''
path = input('输入路径：')
ls = os.listdir(path)

ret = filter(lambda x: os.path.isfile(os.path.join(path,x)) and os.path.getsize(os.path.join(path,x))>10*1024, ls)
print(list(ret))
'''


print('******************************华丽的分割线******************************')

from functools import reduce

'''
ret = reduce(lambda x, y: x+y, [1,2,3,4])
print(ret)
'''

def f(x,y):
	print('x=%s,y=%s'%(x,y))
	return x+y


ret = reduce(f, [1,2,3,4])
print(ret)


ret = reduce(lambda x, y: x-y, [1,2,3,4], 5)
print(ret)

ret = reduce(lambda x, y: x+y, ['aa', 'bb', 'cc'], 'dd')
print(ret)


print('******************************华丽的分割线******************************')
'''
如果是数字，按照数字的大小
如果是字符串，ord函数转成unicode数字进行比较
'''


ls = [11,21,10,4]
ls.sort()
print(ls)

ls = [11,21,10,4]
ls2 = sorted(ls)
print(ls2)

class Person:
	def __init__(self,name,sid):
		self.name = name
		self.sid = sid
	def __str__(self):
		return 'Person name=%s,sid=%s'%(self.name,self.sid)


p1 = Person('老王',1)
p2 = Person('旺财',2)
p3 = Person('小强',3)

persons = [p2,p1,p3]
#persons2 = sorted(persons)

def f(p):
	return p.sid


#persons2 = sorted(persons,key=lambda x:x.sid)
persons2 = sorted(persons,key=f)

for i in persons2:
	print(i)



dicts = [
	{
		'sid':2,
		'name':'a'
	},
	{
		'sid':3,
		'name':'b'
	},
	{
		'sid':1,
		'name':'c'
	}
]

dicts2 = sorted(dicts,key=lambda x:x['sid'])
print(dicts2)




dicts2 = sorted(dicts,key=lambda x:x['sid'],reverse=True)
print(dicts2)