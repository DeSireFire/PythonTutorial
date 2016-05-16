'''

	id(x)：查看地址，得到10进制的数字

	python有一个小整数常量池，-5~~257 
	在python初始化的时候，这些数字就会在内存中了，使用的时候，直接从内存中获取，不会创建新的
	除了这些数字之外，访问一次数字，创建一个新的，既然是新的，地址不一样

'''



'''
a = 1
b = 1
b = 2
print(a)
print(b)
'''

#变量的赋值
num1 = 100
# 右侧是变量的使用，然后是变量的赋值
num2 = num1
#变量的使用
print(num1)
print(num2)

num1 = 200
print(num1)
print(num2)


'''
Traceback (most recent call last):
  File "D:\work\python\2017-06-26\讲课\day02\demo\02_变量\02_变量赋值.py", line 32, in <mo
    print(a)
NameError: name 'a' is not defined

如果变量的使用的时候，如果没有赋值，报错。变量未定义
'''
print(a)