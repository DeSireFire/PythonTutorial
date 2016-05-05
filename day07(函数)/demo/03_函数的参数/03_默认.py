'''
默认：
	在定义形参的时候，直接赋默认值
	在调用的函数，传递实参的时候，可以不传值


	注意：
		非默认值的参数，在 ，默认值参数之前
'''
def f(name,age=18):
	print('name=%s,age=%s'%(name,age))

f('老王',20)
f('老王')


def f(name='老王',age=18):
	print('name=%s,age=%s'%(name,age))

f('xx')
f(age='xx')