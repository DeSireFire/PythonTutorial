'''
	递归：函数内部再调用当前函数
	满足两个条件：
		1、有循环的内容
		2、有跳出的条件


	一般递归和循环都能完成需求。
	递归写起来简洁。效率比较低。
	如果递归的层小。可以可以使用递归。否则使用循环。
'''


'''
	斐波纳契数列
	1,1,2,3,5,8,13,21。。。。。。

	第n个值 = 第(n-1)值+第(n-2)值
	        = (n-2)+(n-3)+(n-3)+(n-4)
'''


'''
def fun(n):
    n1=1
    n2=1
    n3=1
    if n<1:
        print('输入错误！')
        return -1
    while (n-2)>0:
        n3=n1+n2
        n1=n2
        n2=n3
        n-=1
    return n3

num=int(input('请输入第几个数'))
a=fun(num)
print('第%d个数字为：%d'%(num,a))
'''

def fs(n):
	if n==1 or n==2:
		return 1 
	return fs(n-1)+fs(n-2)

print(fs(10))


'''
求阶乘
20! = 20*19!=20*19*18!

n!=n*(n-1)!

'''

def factorial(n):
	if n==1:
		return 1
	return n*factorial(n-1)

print(factorial(200))


def factorial(n):
	ret = 1
	for i in range(2,n+1):
		ret*=i
	return ret
print(factorial(20000))