'''
d = {'name':'老王','age':20,'address':'北京','hoppy':['篮球','乒乓','台球'],'婚否':'是'}
print(d)
print(d['name'])
print(d['hoppy'][1])

d['收入']=10000
print(d)

d.pop('age')
print(d)

del d['address']
print(d)

d.clear()
print(d)
'''
'''
print(d['name'])

c = d.get('names',222)
print (c)
print(d.get('names',1000))
print('&&&&&&&&&&&&&&&&&&&&&&&&')

print(len(d))

print(str(d))

a = d.keys()
print(a)

b = d.values()
print(b)

c = d.items()
print(c)

print('name' in d)

for n in d:
	print('%s:%s'%(n,d[n]))

print('……………………分隔线……………………')
for k in d.keys():
	print('%s,%s'%(k,d[k]))

print('**********分隔线**********')
for k,v in d.items():
	print('%s,%s'%(k,v))

dict1 = {'name':'老王','age':20,'address':'北京'}
dict2 = dict1.copy()
print(dict2)
print(id(dict1))
print(id(dict2))

print('……………………分隔线……………………')
dict1.fromkeys(['name','age','address'])
print(dict1)
dict1.fromkeys(('name','age','address'))
print(dict1)

ret = dict1.setdefault('hoppy','打球')
print(dict1)
print(ret)

dict1 = {'name':'老王','age':20,'address':'北京'}
ret = {'hoppy':'打球','money':5000}
dict1.update(ret)
print(dict1)
print(ret)
'''
a = {1,2,3,45,6,8,9,8,5}
print(a)

a = {1,2,3,3,4,5,6}
b = {5,8,9,11,22,33}
c = a|b
print(c)

d = a&b
print(d)

a = {1,2,3,45,6,8,9,8,5}
a.add(77)
print(a)

a.remove(77)
print(a)

a = {1,2,3,3,4,5,6}
b = {5,8,9,11,22,33}
a.update(b)
print(a)

a = {1,2,3,3,4,5,6}
a.update((78,98))
print(a)

a = {1,2,3,3,4,5,6}
a.discard(6)
print(a)

a = {1,2,3,3,4,5,6}
a.pop()
print(a)

a = {1,2,3,3,4,5,6}
a.clear()
print(a)

a = {1,2,3,3,4,5,6}
b = {5,8,9,11,22,33}
c = a.union(b)
print(c)

a = {1,2,3,3,4,5,6}
b = {5,8,9,11,22,33}
c = a.intersection(b)
print(c)

a = {1,2,3,3,4,5,6}
b = {1,2,3}
c = a.difference(b)
print(c)

a = {1,2,3,3,4,5,6}
b = {1,2,3}
c = b.issubset(a)
print(c)

a = {1,2,3,3,4,5,6}
b = {1,2,3}
c = a.issuperset(b)
print(c)
