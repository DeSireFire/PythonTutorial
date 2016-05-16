'''

1、处理任何的异常

代码
try:
	可能出现异常的代码
except:
	异常的处理
代码



2、处理特定的异常

try:
	可能出现异常的代码
except (异常类1，异常类2):
	异常的处理

按顺序进行异常的捕捉，如果第一个异常类捕捉到了，后面就不再捕捉了。
如果都不能捕捉，报错



try except 会降低代码的运行速度，所以不能将所有的代码都放进去。
只放可能出现异常的代码


说明：
	所有的异常，在python都以各种类进行了描述。
	代码出现了异常，其实是解析器，找到对应的描述类，创建了一个对应的实例对象，然后抛出。


一般在框架中异常的处理：
	1、将异常信息写到文件中，日志文件
	2、继续抛出异常

'''
print('begin...')
try:
	print('1...')
	open(r'C:\Users\Administrator\Desktop\软件\老王.txt','r')
	print('2...')
except:
	print('出现异常了')
print('end...')


print('***************************华丽的分割线***************************')


print('begin...')
try:
	print('1...')
	a+=1		# x=XXError('xxx错了')  raise x
	open(r'C:\Users\Administrator\Desktop\软件\王.txt','r')
	print('2...')
except (NameError,SyntaxError,ZeroDivisionError) as ex:   #ex = x
	print('出现异常了:%s'%ex)
	print(dir(ex))
	print(type(ex))
print('end...')



print('***************************华丽的分割线***************************')


print('begin...')
try:
	print('1...')
	#a+=1		
	open(r'C:\Users\Administrator\Desktop\软件\王.txt','r')
	print('2...')
except NameError as ex:
	print('出现异常了1:%s'%ex)
except SyntaxError as ex:
	print('出现异常了2:%s'%ex)
except ZeroDivisionError as ex:
	print('出现异常了3:%s'%ex)
except FileNotFoundError as ex:
	print('出现异常了4:%s'%ex)
print('end...')

print('***************************华丽的分割线***************************')

print('begin...')
try:
	print('1...')
	open(r'C:\User\Administrator\Desktop\软件\老王.txt','r')
	print('2...')
except Exception as ex:
	print('出现异常了:%s'%ex)
print('end...')


print('***************************华丽的分割线***************************')


print('begin...')
try:
	print('1...')
	#a+=1		
	open(r'C:\Users\Administrator\Desktop\软件\王.txt','r')
	print('2...')
except Exception as ex:
	print('出现异常了1:%s'%ex)
except SyntaxError as ex:
	print('出现异常了2:%s'%ex)
except ZeroDivisionError as ex:
	print('出现异常了3:%s'%ex)
except FileNotFoundError as ex:
	print('出现异常了4:%s'%ex)
print('end...')