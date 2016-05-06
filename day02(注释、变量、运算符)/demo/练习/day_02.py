'''
#数字类型
a = 100
b = 200
d = a+a+b
c = a + b
print(d)
print(c)

m = False
print(False or True)
print(False and True)
print(not True)
print(type(m))
'''
'''
#数字类型转化
a = 1
b = float(a)
print(b)
print(type(b))

a = 1
b = str(a)
print(b)
print(type(b))

a = 1
b = bool(a)
print(b)
print(type(b))


a = 1.1
b = int(a)
print(b)
print(type(b))

a = 1.1
b = bool(a)
print(b)
print(type(b))

a = 1.1
b = str(a)
print(b)
print(type(b))

a = '12.3'
a = float(a)
b = int(a)
print(b)
print(type(b))

#命名方式
Name = '老李'
Adress = '河南'
Email = '234@qq.com'
Age = 28
print(Name,Adress,Email,Age)
'''
'''
#输入输出
name = input('你的名字：')
age = int(input('年龄：'))
adress = input('地址：')
balance = float(input('余额：'))
print('你的名字是：%s,年龄：%d,地址：%s,余额：%0.2f'%(name,age,adress,balance))

name = input('名字：')
age = int(input('年龄：'))
adress = input('居住地：')
balance = float(input('余额：'))
xiaoxi = '你的名字是：%s,年龄：%d,居住地：%s,余额：%0.2f'%(name,age,adress,balance)
print(xiaoxi)
'''
'''
#赋值运算符
a = 100
b = 4
k = 3
c = a + b
d = a - b
e = a * b
f = a / b
g = a ** b
h = a//b
i = a % k
a += 100
b //= 3

print('加法%s,减法%s,乘法%s,除法%s,幂%s,取整%s,高级加%s,高级取整%s,取余数%s'%(c,d,e,f,g,h,a,b,i))

#比较运算符
l = 10
ll = 10
print(l==ll,l!=ll,l>ll,l<ll,l>=ll,l<=ll)
'''

#逻辑与算符
a = True
b = False
print(a and b,a or b,not a, not b)

print(a and 10,b and 10,a or 10, b or 10)

