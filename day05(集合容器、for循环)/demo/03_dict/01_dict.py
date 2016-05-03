'''
	存储咱班所有的人的信息
	编号，姓名，年龄，性别，身高。。。。。
	方便的存储和获取

	唯一定位一个值，快
	对存储信息有说明

	用字典完成
'''

student1=['1','老王',25]
student2=['2','老张',30]
#等等有200个

students=[['1','老王',25],['2','老张',30]]

'''
	语法：
	1、定义字典：键是字符串(不能重复，唯一的)，值是任何类型
	dict = {'key1':值1,'key2':值3,'key3':值3.......}
	2、根据键获取值
	value = dict['key']


	注意：字典的键是无序的，所以，存储的时候，与获取的时候，可能顺序不一致
'''

student1={'id':1,'name':'老王','age':25,'score':59.9}
print(len(student1))
print(student1)
print(student1['name'])

students = [
	{'id':1,'name':'老王','age':25,'score':59.9,'hobby':['抽烟','喝酒','烫头发']},
	{'id':2,'name':'老张','age':15,'score':20,'hobby':['吃','喝']}
]

print(students)		#s = str(students) print(s)
print(students[0]['hobby'][1])

print('*'*40)

student = {'id':1,'name':'老王'}
#新增
student['age'] = 33
print(student)


print('*'*40)

student = {'id':1,'name':'老王'}
#修改
student['id'] = 33
student['id'] = 20
print(student)


print('*'*40)

student = {'id':1,'name':'老王'}
print(student)
#删除，并返回值
sid = student.pop('id')
print(student)
print(sid)


print('*'*40)

student = {'id':1,'name':'老王'}
print(student)
#删除
del student['id']
print(student)


print('*'*40)

student = {'id':1,'name':'老王'}
print(student)
#删除所有，清空
student.clear()
print(student)


print('*'*40)

'''
	查：
		value = dict['key']
		如果键不存在，报错。KeyError: 'idssssss'
'''
student = {'id':1,'name':'老王'}
sid = student['id']
print(sid)

'''
student = {'id':1,'name':'老王'}
sid = student['idssssss']
print(sid)
'''



print('*'*40)

'''
	查：
		value = dict.get('key'[,默认值])
		如果键不存在，返回默认值，默认是None
'''
student = {'id':1,'name':'老王'}
sid = student.get('id')
print(sid)


student = {'id':1,'name':'老王'}
sid = student.get('ids')
print(sid)



student = {'id':1,'name':'老王'}
sid = student.get('ids','未知')
print(sid)


print('*'*40)

'''
	获取所有的键
	获取所有的值
	获取所有的键值对
'''
student = {'id':1,'name':'老王'}
keys = student.keys()
print(type(keys))
print(keys)

for i in keys:
	print(i)

print('*'*40)
student = {'id':1,'name':'老王'}
values = student.values()
print(type(values))
print(values)

for i in values:
	print(i)

print('*'*40)
student = {'id':1,'name':'老王'}
items = student.items()
print(type(items))
print(items)

# items   dict_items([('id', 1), ('name', '老王')])
for i in items:
	print('%s=%s'%(i[0],i[1]))

print('*'*40)
for k,v in items:
	print('%s=%s'%(k,v))


print('*'*40)
student = {'id':1,'name':'老王'}
print('id' in student)
print('id' not in student)