'''
	1、用户选择
	2、计算机随机生成
	3、判断用户的结果

	分析：

		剪刀(0)  石头(1)  布(2)


	赢
		计算机		用户
		0			1
		1			2
		2			0
	输
		计算机		用户
		0			2
		1			0
		2			1
'''
#导入random.py文件
import random
#调用random.randint函数，返回一个随机数
computer = random.randint(0,2)
#用户选择
player = int(input('请输入：剪刀(0)  石头(1)  布(2):'))
#判断
if player!=0 and player!=1 and player!=2:
	print('输入的数字不符合要求，请选择0,1,2')
else:
	if (computer==0 and player==1)or(computer==1 and player==2)or(computer==2 and player==0):
		print('恭喜你，赢啦......')
	elif computer==player:
		print('平手......')
	else:
		print('输啦......')

	print('计算机选择的是%s,用户选择的是%s.'%(computer,player))