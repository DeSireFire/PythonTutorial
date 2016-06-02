import  re

ret1 = re.match('taobao','www.taobao.com')
print(ret1)

ret1 = re.match('taobao','taobao.com')
print(ret1)
print(ret1.group())
print(ret1.span())


# ret = re.match('.','\nabc')
# print(ret.group())

# ret = re.match('\.','abc')
# print(ret.group())

ret = re.match("[hH]","Hello Python")
print(ret.group())

ret = re.match("[h]","Hello Python",re.I)
print(ret.group())

# 匹配0到9第一种写法
ret = re.match("[0123456789]","7Hello Python")
print(ret.group())

# 匹配0到9第二种写法
ret = re.match("[0-9]","7Hello Python")
print(ret.group())

# 匹配非0到9第二种写法
ret = re.match("[^0-9]","Hello Python")
print(ret.group())

ret = re.match("嫦娥\d号","嫦娥1号发射成功")
print(ret.group())


ret = re.match("\w","嫦娥1号发射成功")
print(ret.group())
ret = re.match("\w","a嫦娥1号发射成功")
print(ret.group())
ret = re.match("\w","1嫦娥1号发射成功")
print(ret.group())
ret = re.match("\w","_嫦娥1号发射成功")
print(ret.group())
# ret = re.match("\w",",嫦娥1号发射成功")
# print(ret.group())
ret = re.match("\w","嫦娥1号发射成功",re.A)
print(ret)


ret = re.match("[\u4e00-\u9fa5]","嫦娥1号发射成功")
print(ret)


mm = "c:\\a\\b\\c"
print(re.match("c:\\\\",mm).group())


mm = "c:\\a\\b\\c"
print(re.match(r"c:\\a",mm).group())


mm = r"c:\a\b\c"
print(re.match(r"c:\\a",mm).group())


print(re.match("[A-Z][a-z]*","MmAaBb").group())
print(re.match("[A-Z][a-z]*","MmaaAaBb").group())
print(re.match("[A-Z][a-z]*","MMAaBb").group())

print(re.match("[\w]{4,20}@163\.com$", "xiaoWang@163.comxxxxx"))


print('****************************华丽的分割线****************************')
print(re.match(".*\blove\b", "i love you"))


print(re.match("[1-9]?\d","8"))
print(re.match("[1-9]?\d","78"))
print(re.match("[1-9]?\d","08"))
print(re.match("[1-9]?\d$","08"))

print(re.match("[1-9]?\d$|100","8"))
print(re.match("[1-9]\d$|a","1a"))


ret = re.match("\w{4,20}@(163|126|qq)\.com", "test@163.com")


print(ret.group())
print(ret.group(0))

print(ret.group(1))


ret = re.match(r"([^-]*)-(\d+)","010-12345678")
print(ret.group(1))
print(ret.group(2))
print(ret.group(0))


ret = re.match("<[a-zA-Z]*>\w*</[a-zA-Z]*>", "<html>hh</html>")
print(ret)


ret = re.match("<[a-zA-Z]*>\w*</[a-zA-Z]*>", "<html>hh</htmi>")
print(ret)


ret = re.match(r"<([a-zA-Z]*)>\w*</\1>", "<html>hh</htmi>")
print(ret)

ret = re.match(r"<([a-zA-Z]*)>\w*</\1>", "<html>hh</html>")
print(ret)
print(ret.group(1))


ret = re.match(r"<(\w*)><(\w*)>.*</\2></\1>", "<html><h1>www.taobao.com</h1></html>")
print(ret)

ret = re.match(r"<(?P<r1>\w*)><(?P<r2>\w*)>.*</(?P=r2)></(?P=r1)>", "<html><h1>www.taobao.com</h1></html>")
print(ret)



s1 = '<img src="http://img.mmjpg.com/hot/barbie.jpg" alt="可儿" />'

ret = re.match(r'<img src="(.*)" alt',s1)
print(ret.group())
print(ret.group(1))