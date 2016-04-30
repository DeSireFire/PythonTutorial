'''
变量如何定义和使用

变量名 = 值

运行的顺序，右侧计算得到一个值，赋值给左侧。

python是一个弱类型语言，
在定义变量的时候，不需要先声明类型，变量类型是根据右侧的值来判断的
num = 100
num = 'abc'



比如java，c++都是强类型语言，变量必须先声明类型
赋值的时候，只能赋值对应类型的值
int num = 100
num = "abc"  错误
'''

num = 100
print(num)
print(type(num))
name = '老王'
print(name)
print(type(name))
num = 120
print(num)
num = 'abc'


money = 2.5
print(money)
print(type(money))

a = 1
b = '1'

