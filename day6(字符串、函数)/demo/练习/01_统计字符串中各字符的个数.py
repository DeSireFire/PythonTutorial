'''
统计字符串中，各个字符的个数
比如："hello world" 字符串统计的结果为： h:1 e:1 l:3 o:2 d:1 r:1 w:1
'''

info1 = input('输入一个字符串：')
info2 = set(info1)
info3 = dict.fromkeys(info2,0)
for i in info2:
	info3[i] = info1.count(i)
print(info3)
