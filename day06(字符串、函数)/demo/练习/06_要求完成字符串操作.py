'''
s = "aAsmr3idd4bgs7Dlsf9eAF"

1.请将s字符串的数字取出，并输出成一个新的字符串。
2.请统计s字符串出现的每个字母的出现次数（忽略大小写，a与A是同一个字母），并输出成一个字典。 例 {'a':3,'b':1}
3.请去除s字符串多次出现的字母，仅留最先出现的一个,大小写不敏感。例 'aAsmr3idd4bgs7Dlsf9eAF'，经过去除后，输出 'asmr3id4bg7lf9e'
4.输出s字符串出现频率最高的字母。

'''

s = 'aAsmr3idd4bgs7Dlsf9eAF'
ls1 = []
for i in s:
	if i.isdigit():
		ls1.append(i)
s1 = ''.join(ls1)
print(s1)


s = 'aAsmr3idd4bgs7Dlsf9eAF'
ls2 = []
for i in s.upper():
	if i not in ls2:
		ls2.append(i)
print(ls2)



info1 = s
info2 = set(info1)
info3 = dict.fromkeys(info2,0)
for i in info2:
	info3[i] = info1.count(i)
print(info3)


num=max(info3.values())
for k,v in info3.items():
	if v==num:
		print(k)