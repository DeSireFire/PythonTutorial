# 函数对函数的调用
def a(aa,bb,cc):
	print('你是小猫!!!')
	if(aa<bb):
		aa = bb
	b(aa)
	print('a函数结束!!!')
def b(num):
	print('结果出来啦%s'% num)
a(25,40,36)
