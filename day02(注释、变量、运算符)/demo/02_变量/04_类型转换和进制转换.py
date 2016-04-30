'''
	进制之间的转换，了解即可。
'''


'''
float(x):   返回一个浮点型数字

x可以是整数和字符串
'''

num1 = float(1)
print(num1)
print(type(num1))

num2 = float('123')
print(num2)
print(type(num2))

'''
num3 = float('a')
print(num3)
print(type(num3))
'''



'''
int(x):   返回一个整型数字

x可以是浮点数和字符串
'''

num1 = int(1.9)
print(num1)
print(type(num1))

num2 = int('123')
print(num2)
print(type(num2))


'''
str(x):   返回字符串

x可以是任意类型
'''

s1 = str(1.9)
print(s1)
print(type(s1))

s2 = str(1)
print(s2)
print(type(s2))

s3 = str(True)
print(s3)
print(type(s3))

s4 = str(None)
print(s4)
print(type(s4))

'''
进制转换

2,8,16转10进制
'''
#2进制转10进制
a = '0b110'
ret1 = int(a,2)
print(ret1)
print(type(ret1))

#8进制转10进制
a = '0o110'
ret1 = int(a,8)
print(ret1)
print(type(ret1))

#16进制转10进制
a = '0x110'
ret1 = int(a,16)
print(ret1)
print(type(ret1))


#10进制转2进制
a = 1234
ret1 = bin(a)
print(ret1)
print(type(ret1))

#10进制转8进制
a = 1234
ret1 = oct(a)
print(ret1)
print(type(ret1))

#10进制转16进制
a = 1234
ret1 = hex(a)
print(ret1)
print(type(ret1))


