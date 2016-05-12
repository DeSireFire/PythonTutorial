'''
******一层*******

只有一层深浅拷贝没区别：都是
		1、如果是可变，地址不同
		2、如果是不可变，地址相同


******多层*******


深拷贝：
	copy.deepcopy
	1、如果所有层都是不可变的，所有层地址相同
	2、如果有一个可变的，外层一定不同
	3、如果内层中这一层是可变的，地址不同。否则，地址相同
	

浅拷贝：
	copy.copy
	内层地址一样
	外层地址：
		1、如果是可变，地址不同
		2、如果是不可变，地址相同
	


= 二者地址一样，指向同一个



可变对象：
	1、列表、字典、set、对象
	2、数字、字符串、元组、None、bool
'''

ls1 = [1,2,3]
ls2 = ls1
print(id(ls1))
print(id(ls2))

print('*********************华丽的分割线*********************')





import copy

ls1 = [1,2,3]
ls2 = copy.copy(ls1)			#地址不同
print(id(ls1))
print(id(ls2))


ls1 = (1,2,3)
ls2 = copy.copy(ls1)			#地址相同
print(id(ls1))
print(id(ls2))




a = [1,2,3]
b = [4,5,6]
ls1 = [a,b]
ls2 = copy.copy(ls1)			#外层地址不同，内层地址相同		
print(id(ls1))
print(id(ls2))

a.append(100)
print(ls1)
print(ls2)
#print(id(ls1[0]))
#print(id(ls2[0]))



a = [1,2,3]
b = [4,5,6]
ls1 = (a,b)
ls2 = copy.copy(ls1)			#外层地址一样，内层地址相同		
print(id(ls1))
print(id(ls2))

a.append(100)
print(ls1)
print(ls2)
#print(id(ls1[0]))
#print(id(ls2[0]))



a = (1,2,3)
b = (4,5,6)
ls1 = [a,b]
ls2 = copy.copy(ls1)			#外层地址不同，内层地址相同		
print(id(ls1))
print(id(ls2))


print(id(ls1[0]))
print(id(ls2[0]))



a = (1,2,3)
b = (4,5,6)
ls1 = (a,b)
ls2 = copy.copy(ls1)			#外层地址一样，内层地址相同		
print(id(ls1))
print(id(ls2))


print(id(ls1[0]))
print(id(ls2[0]))


print('*********************华丽的分割线*********************')



import copy

ls1 = [1,2,3]
ls2 = copy.deepcopy(ls1)			#地址不同
print(id(ls1))
print(id(ls2))

ls1 = (1,2,3)
ls2 = copy.deepcopy(ls1)			#地址相同
print(id(ls1))
print(id(ls2))


print('*'*20)

a = [1,2,3]
b = [4,5,6]
ls1 = [a,b]
ls2 = copy.deepcopy(ls1)			#外层地址不同，内层地址不同	
print(id(ls1))
print(id(ls2))
print(id(ls1[0]))
print(id(ls2[0]))

print('*'*20)

a = [1,2,3]
b = [4,5,6]
ls1 = (a,b)
ls2 = copy.deepcopy(ls1)			#外层地址不同，内层地址不同	
print(id(ls1))
print(id(ls2))
print(id(ls1[0]))
print(id(ls2[0]))


print('*'*20)

a = (1,2,3)
b = (4,5,6)
ls1 = [a,b]
ls2 = copy.deepcopy(ls1)			#外层地址不同，内层地址相同		
print(id(ls1))
print(id(ls2))
print(id(ls1[0]))
print(id(ls2[0]))


print('*'*20)

a = (1,2,3)
b = (4,5,6)
ls1 = (a,b)
ls2 = copy.deepcopy(ls1)			#外层地址一样，内层地址相同		
print(id(ls1))
print(id(ls2))
print(id(ls1[0]))
print(id(ls2[0]))