'''
list = [1,2,3,4,5,6]
list.append(3)
print(list)

lala = list.index(3)
print(lala)

print(list[5])

print(list.count(3))

lenth = len(list)
print(lenth)

print(max(list),min(list))

list.insert(1,9)
print(list)

list.extend([10,12,15])
print(list)

aaa = [1,2,'nihao',3,[11,14,15,['老王'],18]]
print(aaa[4][3])
'''
'''
aaa = [1,2,'nihao',3,[11,14,15,['老王'],18],55]
aaa.pop()
print(aaa)

aaa.pop(1)
print(aaa)

del aaa[0]
print(aaa)

aaa.remove(3)
print(aaa)
'''
'''
b = [1,2,5,4,3,9,6,8,7,11,45,25] 
b.sort()
print(b)
b.reverse()
print(b)
c = b[1:12:2]
print(c)

k = b[2:10]
print(k)
f = b[:11]
print(f)
d = b[:11:3]
print(d)
'''
'''
a = tuple([1,2,3])
c = list((4,5,6))

print(c,a)
print(11 in a)

print([14,15,16]+[1,2,3])
print('hello\000'*3)
'''
'''
nums = ([1,2,3,4],'老王')
nums[0][3] = 66
print(nums)
print(type(nums))
'''
'''
a = [1,2,3,4,5,6,7,8,9]
i = 0
while i<=8:
	print(a[i],'\000',end='')
	i+=1
print()

for dd in a:
	print ('结果是:',dd,'\000',end='')
print()

a.sort(reverse=True)
print(a)
'''

'''
dict={1:'a',2:'b',3:'c',4:'d'}
print(dict)

a = dict.pop(2)
print(a)

del dict[3]
print(dict)

dict.clear()
print(dict)

dict1={1:'a',2:'b',3:'c',4:'d'}
print(len(dict1))

print(str(dict1))

print(dict1.keys())

print(dict1.values())

print(dict1.items())
'''
'''
a = 10
b = a
b = 11
print(a)
print(b)

a = [1,2,3,4]
b = a 
b.append(5)
print(a)
print(b)

a = [1,2,3,4]
b = a 
b = [2,3,1,6]
print(a)
print(b)

a = 10
b = a
a = 20
print(a)
print(b)
'''

