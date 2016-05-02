'''
	dict循环遍历的三种方式
'''


nums = [2343,55,11]
for i in nums:
	print(i)

print('*'*40)
student = {'id':1,'name':'老王','age':22}

for key in student:
	print('%s:%s'%(key,student[key]))

print('*'*40)
student = {'id':1,'name':'老王','age':22}

for key in student.keys():
	print('%s:%s'%(key,student[key]))


print('*'*40)
student = {'id':1,'name':'老王','age':22}

for key,value in student.items():
	print('%s:%s'%(key,value))


