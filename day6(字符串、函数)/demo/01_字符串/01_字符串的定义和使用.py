'''
字符串使用单引号和双引号引起来的内容。
推荐使用单引号
'''

name = 'abc老王'
print('字符串的长度(粒度：字符):%s'%(len(name)))

print(name[1])
print(name[-1])
print(name[0:])


'''
格式化

'''
name = '老王'
age = 20

info = '名字=%s,年龄=%s,16进制=%x'%(name,age,age)
print(info)


'''
转移字符

\作为转义字符,将一个特殊意义的字符，转成普通的字符
'''
name = '"老王"'
print(name)

name = '\'老王\''
print(name)


name = '老\王'
print(name)

name = '老\\t王'
print(name)

print(len('\t'))


info = '《静夜思》\n床前明月光\n疑是地上霜\n举头望明月\n低头思故乡'
print(info)
print(len(info))

info='''《静夜思》
床前明月光
疑是地上霜
举头望明月
低头思故乡'''
print(info)
print(len(info))


'''
+
*
'''

a = 'a'+'b'+'c'
print(a)

a = '-'*100
print(a)
