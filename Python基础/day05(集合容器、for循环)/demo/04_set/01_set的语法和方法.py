'''
	set集合是 无序，不能重复的集合
'''
set1 = {1,234,4}
print(type(set1))


set1.add(120)
print(set1)

set1.remove(234)
print(set1)


print('*'*40)

s1 = {1,2,3}
s2 = {2,3,4}
ret = s1|s2
print(ret)

ret = s1&s2
print(ret)

ret = s1-s2
print(ret)


print('*'*40)
print(type(()))
print(type([]))
print(type({}))
print(type(set()))

#如果元组只有一个值，必须加,
names=('老王',)
print(type(names))

print('*'*40)
s1 = {1,2,3}
s2 = {2,3,4}
s1.update(s2)
print(s1)


s1 = {1,2,3}
s1.update([1,1,1,23,4,45,556])
print(s1)




'''
	list与set之间的转换

	list(),tuple(),set()
'''

list1 = [1,1,23,444,1]
set1 = set(list1)
print(set1)
list2 = list(set1)
print(list2)

'''
	多维
'''

nums=[[1,2,3],[33,[333,456],10]]
print(nums[1][1][1])



'''

	1、list		可变，有序，可重复
	2、tuple	将list的[]变成(),不可变，有序，可重复
	3、dict		键值对	可变
	4、set		可变，无序，不可重复


	list() tuple() set()相互转换
'''
