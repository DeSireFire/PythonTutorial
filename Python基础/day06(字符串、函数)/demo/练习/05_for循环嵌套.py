'''
三色球问题
有红、黄、蓝三种颜色的求，其中红球 3 个，黄球 3 个，绿球 6 个。先将这 12 个球混合放在一个盒子中，从中任意摸出 8 个球，编程计算摸出球的各种颜色搭配。

遍历所有的情况
'''
for a in range(0,4):
	for b in range(0,4): 
		for c in range(0,7):
			if a+b+c==8:
				print(a,b,c)
