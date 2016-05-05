'''
s = "aAsmr3idd4bgs7Dlsf9eAF"
1.请将s字符串的数字取出，并输出成一个新的字符串。
2.请统计s字符串出现的每个字母的出现次数（忽略大小写，a与A是同一个字母），
  并输出成一个字典。 例 {'a':3,'b':1}
3.请去除s字符串多次出现的字母，仅留最先出现的一个,大小写不敏感。
  例 'aAsmr3idd4bgs7Dlsf9eAF'，经过去除后，输出 'asmr3id4bg7lf9e'
4.输出s字符串出现频率最高的字母。
'''

#1.0
s = "aAsmr3idd4bgs7Dlsf9eAF"
a = list(s)
for i in a:
	if i.isdigit():
		a.remove(i)
d = ''.join(a)
print(d)
#2.0
d.lower()
m = list(d)
b = {}
for k in d:
	b[k]=m.count(k)
print(b)
#3.0
s = s.lower()
aa = list(s)
max=1
for i in aa:
	if aa.count(i)>max:
		max = aa.count(i)
aa.reverse()
mm = 1
while mm<max:
	for m in aa:
		if aa.count(m)>1:
			aa.remove(m)
	mm+=1
aa.reverse()
bb = ''.join(aa)
print(bb)

#4.0

aa = list(s)
max=1
for i in aa:
	if aa.count(i)>max:
		max = aa.count(i)
		print(i,'\000',end='')


