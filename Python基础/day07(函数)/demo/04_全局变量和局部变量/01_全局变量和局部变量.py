'''
	变量：
		全局变量
			1、定义在函数的外面
			2、定义在函数的内部，并使用global声明


			作用域：
				整个py都能访问，在访问之前只要赋值就行
			
		局部变量
			1、定义在函数的内部（包括形参）

			作用域：
				只能在函数内部调用，函数结束，消失。

	
'''

num = 100
print(num)

def f1():
	print('f1...num=%s'%num)
f1()




def f2(a):
	print('f2...a=%s'%a)
f2(100)


def f3():
	a = 110
	print('f3...a=%s'%a)
f3()
#print(a)


if 1>2:
	num1 = 100
else:
	num1 = 200

print(num1)



for i in range(100):
	pass

print(i)