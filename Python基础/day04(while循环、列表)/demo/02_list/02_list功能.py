#定义列表
nums = [1,2,88,34,55,11,3333,88]
#通过下标获取值[0----len)
num = nums[4]
print(num)
'''
	通过值，获取下标
	index()
	只获取第一次出现的位置
	如果这个值不存在，报错ValueError: 1111111 is not in list
'''
where = nums.index(88)
print(where)
'''
	count()，可以获取此值在list列表中的个数
	如果没有就是0
'''
num = nums.count(888)
print(num)
'''
	最大值max()，最小值min()
'''
n1 = max(nums)
n2 = min(nums)
print(n1)
print(n2)
print(max(10,20,99))

'''
	append() 在list末尾添加值
	带小括号都是函数(不完全对)
	有的有返回值，有的没有返回值(None)。
	就算有返回值，根据需要是否接收。
'''
nums = [1,2,88,34,55,11,3333,88]
nums.append(110)
print(nums)

'''
	insert() 可以插入到指定位置
'''
nums = [1,2,88,34,55,11,3333,88]
#nums.insert(2,110)
nums.insert(-2,110)
print(nums)

'''
	extend() 将一个列表里的所有的内容放到另一个列表中
'''
num1 = [1,2,3]
num2 = [4,5,6]

num1.extend(num2)
print(num1)


num1 = [1,2,3]
num2 = [4,5,6]

num1.append(num2)
#[1, 2, 3, [4, 5, 6]]
print(num1)

'''
ls = num1[3]
num = ls[1]
print(num)
'''
print(num1[3][1])

nums = [1,[123,44,[333,444,55,[44,113,55555]]]]
print(nums[1][2][3][2])

'''
	修改，通过下标访问
'''	
nums = [1,2,3]
print(nums)
nums[1]=110
print(nums)


'''
	pop()删除，并返回此删除的值
	如果不写下标，删除最后一个
	如果写下标，就删除对应下标的内容

'''
nums = [110,120,119]
num = nums.pop()
print(num)
print(nums)


nums = [110,120,119]
num = nums.pop(1)
print(num)
print(nums)


'''
	del 列表[下标]
	删除列表中指定下标的值
'''
nums = [110,120,119]
del nums[1]
#del(nums[1])
print(nums)

'''
a = 1
del a
print(a)
'''

'''
	remove()根据值进行删除
'''
nums = [110,120,119]
nums.remove(120)
print(nums)


'''
	in
	not in
	判断是否存在
'''
nums = [110,120,119]
#ret = 110 in nums
ret = 110 not in nums
print(ret)

'''
	求一个值，在列表中的所有的下标？
'''

'''
	脚本
	+
	*
'''
num1 = [1,2,3]
num2 = [4,5,6]
ret = num1+num2
print(ret)

num1=['老王','laowang']
ret = num1*2
print(ret)


'''
	reverse() 反向
	sort()	  排序
'''
nums = [110,120,119]
nums.reverse()
print(nums)


nums = [110,120,119]
nums.sort()
#nums.reverse()
print(nums)

'''
	字母，汉字是按照编码数字进行比较
'''
nums = ['bba','abc','abd']
nums.sort()
print(nums)

nums = ['旺财','老王','隔壁']
nums.sort()
print(nums)

nums = ['1','老王','3']
nums.sort()
print(nums)


'''
	切片,返回一个新的list
	测试，记住
	[a:b:c]
'''
nums = [1,2,88,34,55,11,3333,88]
ret = nums[0:4]
print(ret)



nums = [1,2,88,34,55,11,3333,88]
ret = nums[0:len(nums)]
print(ret)


nums = [1,2,88,34,55,11,3333,88]
ret = nums[0:100]
print(ret)


nums = [1,2,88,34,55,11,3333,88]
ret = nums[0:]
print(ret)



nums = [1,2,88,34,55,11,3333,88]
ret = nums[0:len(nums):2]
print(ret)

nums = [1,2,88,34,55,11,3333,88]
ret = nums[:]
print(ret)

nums = [1,2,88,34,55,11,3333,88]
ret = nums[::-1]
print(ret)


nums = [1,2,88,34,55,11,3333,88]
ret = nums[-1:]
print(ret)

nums = [1,2,88,34,55,11,3333,88]
ret = nums[:-1]
print(ret)


nums = [1,2,88,34,55,11,3333,88]
ret = nums[::-2]
print(ret)




