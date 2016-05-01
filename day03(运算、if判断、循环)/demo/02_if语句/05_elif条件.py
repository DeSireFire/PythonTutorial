'''
	if 条件:
		语句
	elif 条件：
		语句
	elif 条件：
		语句
	elif 条件：
		语句
	else:
		语句
'''
'''
	3000以下：屌丝
	3000-5000：土鳖
	5000-8000：温饱
	8000-12000：普通
	12000-20000：小康
	20000——		：土豪
'''
salary = int(input('输入工资：'))
if salary<3000:
	print('屌丝......')
elif salary<5000:
	print('土鳖......')
elif salary<8000:
	print('温饱......')
elif salary<12000:
	print('普通......')
elif salary<20000:
	print('小康......')
else:
	print('土豪......')

'''
	0-100

	60以下：E
	60-70：D
	70-80：C
	80-90：B
	90-100：A
'''
score = int(input('输入分数：'))
if score>=0 and score<=100:
	if score<60:
		print('E......')
	elif score<70:
		print('D......')
	elif score<80:
		print('C......')
	elif score<90:
		print('B......')
	else:
		print('A......')
else:
	print('分数只能是0-100之间，你是从火星来的吗')
