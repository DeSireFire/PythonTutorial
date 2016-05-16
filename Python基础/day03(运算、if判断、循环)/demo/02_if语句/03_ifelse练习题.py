'''
if 条件:
	语句
else:
	语句
'''
'''
1、输入一个年份，判断是否是闰年
	条件：
		1、能被4整除，不能被100整除  year%4==0 and year%100!=0
		or
		2、能被400整除				 year%400==0
'''
year = int(input('输入一个年份：'))
if (year%4==0 and year%100!=0) or (year%400==0):
	print('闰年')
else:
	print('平年')


'''
2、输入工资，如果工资在10000-20000之间，就是小康。
   否则，土豪或者土鳖
'''
salary = int(input('输入工资：'))
#if 20000>=salary>=10000:
if salary>=10000 and salary<=20000:
	print('小康')
else:
	print('土豪或者土鳖')
