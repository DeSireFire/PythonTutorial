'''
find		从左面找第一次出现的位置
rfind		从右面找第一次出现的位置
找不到返回-1


index
rindex
功能和find一样，但是找不到会报错，一般不用

下标依然从左面0开始
'''

info = '今天，中华人民共和国今天终于成立中国啦'
sub_info = '今天'

index1 = info.find(sub_info)
print(index1)

index1 = info.find(sub_info,-9,-1)
print(index1)


index1 = info.find(sub_info,3)
print(index1)

index1 = info.rfind(sub_info)
print(index1)


index1 = info.rfind('老王')
print(index1)



index1 = info.index(sub_info)
print(index1)

'''
index1 = info.index('老王')
print(index1)
'''


print('**************************华丽的分割线**************************')

'''
count
统计次数
'''
info = '今天，中华人民共和国今天终于成立中国啦'
sub_info = '今天'
num = info.count(sub_info)
print(num)


print('**************************华丽的分割线**************************')

'''
字符串的遍历
'''
info = '今天，中华人民共和国今天终于成立中国啦'
for i in info:
	print(i)

print('**************************华丽的分割线**************************')

'''
split
按照固定字符分隔,返回一个列表

splitlines
按照换行符分割

partition
从左面分割一个，左中右都保留
rpartition
从右面分割一个，左中右都保留
'''
hobby = '抽烟-烫头发-喝酒'
ret = hobby.split('-')
print(type(ret))
print(ret)


hobby = '抽烟-烫头发-喝酒'
ret = hobby.split('abc')
print(type(ret))
print(ret)


hobby = '抽烟，烫头发，喝酒'
ret = hobby.split('，')
print(type(ret))
print(ret)

info = '《静夜思》\n\n床前明月光\n疑是地上霜\n举头望明月\n低头思故乡'
ls = info.split('\n')
print(ls)


info = '《静夜思》\n\n床前明月光\n疑是地上霜\n举头望明月\n低头思故乡'
ls = info.splitlines()
print(ls)


info='''《静夜思》
床前明月光
疑是地上霜
举头望明月
低头思故乡'''
ls = info.splitlines()
print(ls)


info = '《静夜思》\r\n床前明月光\r\n疑是地上霜\r\n举头望明月\r\n低头思故乡'
print(info)
ls = info.split('\n')
print(ls)


info = '《静夜思》\r\n床前明月光\r\n疑是地上霜\r\n举头望明月\r\n低头思故乡'
print(info)
ls = info.splitlines()
print(ls)


hobby = '抽烟-烫头发-喝酒'
ret = hobby.partition('-')
print(type(ret))
print(ret)

hobby = '抽烟-烫头发-喝酒'
ret = hobby.rpartition('-')
print(type(ret))
print(ret)


print('**************************华丽的分割线**************************')

'''
startswith
开头

endswith
结尾

isalnum
判断是否是字符和数字

isupper
大写

islower
小写

isspace
'''
info = '我叫老王.jpg'
print(info.startswith('你'))
print(info.endswith('.jpg'))


print('abc123中文'.isalnum())
print('abc中文'.isalpha())
print('1243'.isdigit())


print('ABC123中文'.isupper())
print('abc123中文'.islower())


print('        '.isspace())
print('\t'.isspace())
print('\n'.isspace())

print('**************************华丽的分割线**************************')
'''
capitalize 
首字母大写

upper
全大写

lower
全小写
'''
name = 'abc'
print(name.capitalize())
print(name[0].upper()+name[1:])
print(name)
print(name.upper())
print(name.lower())


print('**************************华丽的分割线**************************')
'''
ljust
rjust
center
'''
info = 'abc'
ret = info.ljust(10)
print(ret+'-')

info = 'abc'
ret = info.rjust(10)
print('-'+ret)


info = 'abc'
ret = info.center(11)
print('-'+ret+'-')
print('**************************华丽的分割线**************************')
'''
strip
裁剪，默认裁剪左右空格
lstrip
左裁剪
rstrip
右裁剪
'''
#name = input('输入姓名：')
name = '  老 王   '
name = name.strip(' ')
#name = name.strip()
print('-'+name+'-')


name = '**老 王****'
name = name.strip('*')
print(name)

print('**************************华丽的分割线**************************')
'''
join
'''

info = '吃-喝-玩-乐'
print(info.split('-'))

ls = ['吃', '喝', '玩', '乐']
info = '-'.join(ls)
print(info)


'''
encode
编码
字符串--->字节

decode
解码
字节--->字符串
'''
info = '我还活着'
ret = info.encode()
print(type(ret))
print(ret)

info = 'abc123我还活着'
ret = info.encode('utf-8')
print(type(ret))
print(ret)


info = b'abc123'
print(info)
print(type(info))


info = 'abc123我还活着'
ret1 = info.encode('utf-8')
ret2 = ret1.decode('utf-8')
print(ret2)
