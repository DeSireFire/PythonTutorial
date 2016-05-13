'''
	生成器：Generator
		保存算法的，可以推算出下一个

	生成器是可以迭代的(Iterable)
	



	Iterable:
	使用for循环从对象的第一个元素开始访问，直到所有的元素被访问完结束。
	迭代器只能往前不会后退。


	迭代器Iterator：
		可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator
		迭代器都是可迭代的，（for循环迭代）

	可迭代的不一定是迭代器，迭代器一定可以迭代
	生成器也是迭代器
'''


'''
生成器是可以迭代的(Iterable)
isinstance(obj,collections.Iterable)只要为True
obj就可以使用for遍历迭代
'''
import collections

ls = [1,2,3]
print(isinstance(ls,collections.Iterable))


from collections import Iterable,Iterator

print(isinstance(ls,Iterable))


print(isinstance(tuple(),Iterable))
print(isinstance(list(),Iterable))
print(isinstance(dict(),Iterable))
print(isinstance(set(),Iterable))
print(isinstance('',Iterable))
print(isinstance(range(10),Iterable))
print(isinstance((x for x in range(10)),Iterable))


print('***************************************华丽的分割线***************************************')

print(isinstance(tuple(),Iterator))
print(isinstance(list(),Iterator))
print(isinstance(dict(),Iterator))
print(isinstance(set(),Iterator))
print(isinstance('',Iterator))
print(isinstance(range(10),Iterator))
print(isinstance((x for x in range(10)),Iterator))

print('***************************************华丽的分割线***************************************')

ls = [110,119,120]

for i in ls:
	print(i)

print('***************************************华丽的分割线***************************************')

ls = [110,119,120]

it = iter(ls)
print(it)
print(next(it))
print(next(it))
print(next(it))
#print(next(it))



set1 = {110,119,120}

it = iter(set1)
print(it)
print(next(it))



print('***************************************华丽的分割线***************************************')
'''
生成器也是迭代器，都是保存算法，可以推算出下一个值。

生成器可以自定义算法。
iter函数可以将目前的大数据集合转成迭代器，使用next获取里的值，避免大数据集合占用过多的内存。

'''
#it = iter([1,2,434534,4545..........])
