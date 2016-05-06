'''
a = '窗前明月光\n疑是地上霜\n举头望明月\n低头思故乡'
print(a)
print(len(a))

#b = '''
#窗前明月光
#疑是地上霜
#举头望明月
#低头思故乡
'''

print(b)
print(len(b))

name = '老王'
print(name)
name = '老\t王'
print(name)
name = '老\\t王'
print(name)
name = '"老王"'
print(name)
name = '\'老王\''
print(name)

print('A\t'*10)
'''
'''
a = 'abcdfauiyapflj'
a = a.split('a')
print(a)
print(type(a))

a = 'a-c-b-d-f'
print(a.count('-',0,8))
print(a.count('-'))

a = 'a-c-b-d-f'
print(a.count('-',2))
print(a.count('-'))


a = 'a\nc-b-d-f'
a = a.splitlines()
print(a)

a = 'sdfsagfdiawhoi'
print(a.partition('a'))


a = 'sdfsagfdiawhoi'
print(a.rpartition('a'))

a = '2sdfsagfdiawhoi'
a = a.startswith('1')
print(a)

a = 'safgsdj3452'
print(a.isalnum())
print(a.isalpha())
print(a.isdigit())
a = 'safadfsf'
print(a.isupper())
print(a.islower())
a = '   '
print(a.isspace())
a = '   \t\n'
print(a.isspace())

a = 'egterf'
a = a.ljust(10)
print(a)
print(len(a))

a = 'egterf'
a = a.rjust(10)
print(a)
print(len(a))

a = 'egterf'
a = a.center(10)
print(a)
print(len(a))

a = 'wang'
print(a.capitalize())
print(a.upper())
print(a.lower())

a = 'ab'
print(a.join('hfdjsh'))

a = 'das324老来乐'
b = a.encode()
print(b)
print(b.decode())

a = 'wgterf'
print(a.rindex('t'))
print(a.swapcase())
print(a.istitle())
'''

def c(a):
	b = 10
d = 3
c(d)
print(d)

def lala(ll):
	ll.append([1,2,3])
	print('函数内取值:',ll)
	return
la = [11,12,13]
lala(la)
print('函数外取值:',la)

def num(a):
	b = 10
	a += b
	return a

print(num(200))

def kk(a,b):
	'''
	吸烟喝酒烫头发
	'''
	la = a
	if(la<b):
		la = b
	print(la)
	return la

print(kk(20,25))
help(kk)

def k(a,b):
	a = a + b
a = 20
b = 30
k(a,b)
print(a)

def k(a,b):
	a.append(b)
a = [20,78,98]
b = [34,45]
k(a,b)
print(a)

def k(a,b):
	a.extend(b)
a = [20,78,98]
b = [34,45]
k(a,b)
print(a)

