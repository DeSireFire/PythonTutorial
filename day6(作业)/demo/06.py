'''
遍历所有的情况
'''
for a in range(0,4):
	for b in range(0,4): 
		for c in range(0,7):
			if a+b+c==8:
				print(a,b,c)