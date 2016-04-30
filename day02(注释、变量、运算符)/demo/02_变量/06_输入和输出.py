'''
	print是输出到控制台，一般测试的时候。
'''

print('刷我滴卡---泰语，你好的意思',end='')
print('呀咩跌---日语，不要的意思')
print('床前明月\n光疑是地上霜')

userName = '老王'
userAge = 40
money = 3.567

'''
	占位符：
		%s  字符串
		%d	整数
		%f  浮点数

'''
#info = '我的名字是叫：'+userName+'，我住在隔壁，我的年龄是：'+userAge
#info = '名字：%s，年龄：%d，余额：%f'%(userName,userAge,money)
#info = '名字：%s，年龄：%s，余额：%s'%(userName,userAge,money)
info = '名字：%s，年龄：%d，余额：%0.2f'%(userName,userAge,money)
info = '名字：%s'%userName
print(info)

print('名字：%s，年龄：%d，余额：%0.2f'%(userName,userAge,money))


'''
输入
input运行到这，程序会阻塞(停止)，等待用户输入并回车。
用户回车后，会将用户输入的内容以字符串形式返回。
不输入内容，直接回车，得到一个空字符串''
'''
#print('呵呵。。。。。')
#name = input('请输入姓名：')
#print('name=%s'%name)
#print('哈哈。。。。。')

'''
num1 = input('输入第一个值:')
num1 = int(num1)
num2 = input('输入第二个值:')
num2 = int(num2)
ret = num1+num2
print(ret)
'''



num1 = int(input('输入第一个值:'))
num2 = int(input('输入第二个值:'))
ret = num1+num2
print('%s+%s=%s'%(num1,num2,ret))