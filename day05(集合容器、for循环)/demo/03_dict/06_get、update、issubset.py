# 字典练习

# get() 函数返回指定键的值，如果值不在字典中返回默认值
# key -- 字典中要查找的键。
# default -- 如果指定键的值不存在时，返回该默认值值。
d = {'name':'老王','age':20,'address':'北京','hoppy':['篮球','乒乓','台球'],'婚否':'是'}
c = d.get('name',200)
# 如果没有name键，返回200
print(c)

# 更新字典
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

# 方法用于判断集合的所有元素是否都包含在指定集合中，如果是则返回 True，否则返回 False
a = {1,2,3,3,4,5,6}
b = {1,2,3}
c = b.issubset(a)
print(c)

a = {1,2,3,3,4,5,6}
b = {1,2,3}
c = a.issuperset(b)
print(c)
