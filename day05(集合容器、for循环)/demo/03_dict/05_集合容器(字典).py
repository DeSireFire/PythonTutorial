my_dict = {}

my_dict['a'] = '233'
print(my_dict)

my_dict['a'] = '666'
print(my_dict)

my_dict['b'] = '888'
print(my_dict)

p = my_dict.pop('a')
print(p)
print(my_dict)

del my_dict['b']
print(my_dict)

rec = dict(map(lambda x,y:(x,y),[chr(i) for i in range(97,123)],range(1,27)))
print(rec)

rec.clear()
print(rec)

my_dict = dict(map(lambda x,y:(x,y),[chr(i) for i in range(97,123)],range(1,27)))
key = my_dict['a']
print(key)

print(len(my_dict))

print(str(my_dict))

a = my_dict.keys()
print(a)
print(list(a))

b = my_dict.values()
print(b)
print(list(b))

c = my_dict.items()
print(c)
print(list(c))

# 使用for循环遍历的三种方式
for key in my_dict:
    print('%s:%s'%(key,dict[key]))

for key in my_dict.keys():
    print('%s:%s'%(key,dict[key]))

for k,v in my_dict.items():
    print('%s:%s'%(k,v))
