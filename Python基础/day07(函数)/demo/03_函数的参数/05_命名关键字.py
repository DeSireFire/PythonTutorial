'''
	命名关键字：
		调用的时候，找到特定的参数赋值
'''

def f(name,age):
	print('name=%s,age=%s'%(name,age))


f(age=18,name='老王')



def person(name, age ,city, *,job):
    print(name, age, city, job)

person('老王',18,'河北',job='游手好闲')


