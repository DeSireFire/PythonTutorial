def test1():
    print("--- in test1 func----")

#调用函数
test1()

#引用函数
ret = test1

print(id(ret))
print(id(test1))

#通过引用调用函数
ret()


print('***************************************华丽的分割线***************************************')

'''
闭包：
	1、函数内部再定义函数,并返回
	2、内部函数引用了外部函数的局部变量
'''

def outer(num):
	def inner():
		print(num)
	return inner


ret = outer(110)
ret()

print('***************************************华丽的分割线***************************************')

#定义一个函数
def test(number):
    #在函数内部再定义一个函数，并且这个函数用到了外边函数的变量，那么将这个函数以及用到的一些变量称之为闭包
    def test_in(number_in):
        print("in test_in 函数, number_in is %d"%number_in)
        return number+number_in
    #其实这里返回的就是闭包的结果
    return test_in


#给test函数赋值，这个20就是给参数number
ret = test(20)

#注意这里的100其实给参数number_in
print(ret(100))

#注意这里的200其实给参数number_in
print(ret(200))


print('***************************************华丽的分割线***************************************')
'''
	提高扩展性
		
	闭包语法的特点：
	1、函数内部再定义函数,并返回
	2、内部函数引用了外部函数的局部变量


	通过引用外部函数的局部变量，可以根据这些值来改变内部函数的业务逻辑，达到完成不同的需求。
	功能得到了扩展。

'''
def line(a,b,x):
	return a*x+b


def line(a,b):
	def inner(x):
		return a*x+b
	return inner


line1 = line(1,-2)
print(line1(10))
print(line1(100))


line2 = line(-3,3)
print(line2(10))


class Line:
	def __init__(self,a,b):
		self.a = a
		self.b = b
	def getY(self,x):
		return self.a*x+self.b

line1 = Line(1,-2)
print(line1.getY(10))