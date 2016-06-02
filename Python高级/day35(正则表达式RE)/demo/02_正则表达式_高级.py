import  re


# 如果一个正则表达式多次使用，可以先编译，再多次使用
pattern1 = re.compile(r'\d+')
ret1 = pattern1.match('1234')
print(ret1)

ret2 = re.match(r'\d+','1234')
print(ret2)


pattern = re.compile(r'([a-z]+) +([a-z]+)', re.I)
m = pattern.match('Hello  World Wide Web')
print(m.group())


pattern = re.compile('\d+')
m = pattern.search('one12twothree34four')
print(m)


pattern = re.compile(r'\d+')   # 查找数字
result1 = pattern.findall('hello 123456 789')
result2 = pattern.findall('one1two2three3four4', 0, 10)
print (result1)
print (result2)


pattern = re.compile(r'\d+')
iter1 = pattern.finditer('hello 123456 789')
print(iter1)
for i in iter1:
    print(i.span(),i.group())


p = re.compile(r'(\w+) (\w+)')
s = 'hello 123, hello 456'

ret = p.sub('laowang',s)
print(ret)


ret = p.sub(r'\2-\1',s)
print(ret)


p = re.compile(r'\d+')
ret = p.sub('124','python=123')
print(ret)


p = re.compile(r'\d+')
ret = p.sub('124','python=123,java=100')
print(ret)


def add(temp):
    #print('temp:',temp)
    num = int(temp.group())
    num+=1
    return str(num)

p = re.compile(r'\d+')
ret = p.sub(add,'python=123,java=100')
print(ret)


p = re.compile(r'\d+')
ret = p.sub('124','python=123,java=100')
print(ret)


p = re.compile(r'[\s\,\;]+')
print(p.split('a,b;; c ,  d'))


p = re.compile(r'\d+')
print(p.match('123456abc'))

p = re.compile(r'\d+?')
print(p.match('123456abc'))

p = re.compile(r'\d*')
print(p.match('123456abc'))

p = re.compile(r'(\d*?)[a]')
print(p.match('123456abc').group(1))


img = '<img data-original="https://rpic.douyucdn.cn/appCovers/2016/11/13/1213973_201611131917_small.jpg" src="https://rpic.douyucdn.cn/appCovers/2016/11/13/1213973_201611131917_small.jpg" style="display: inline;">'
pattern = re.compile(r'src="(.*?)"')
ret = pattern.search(img)
print(ret.group(1))

a = re.split(r'(\d+)(.*)','2323dddd')
print(a)

ret = re.split(r"info","info:xiaoZhang 33          shandong")
print(ret)