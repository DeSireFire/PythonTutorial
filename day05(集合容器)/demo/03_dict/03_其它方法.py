student1 = {'id':1,'name':'老王','age':22}
student2 = student1
print(id(student1))
print(id(student2))
student1['id']=110

print(student1)
print(student2)

print('*'*40)
student1 = {'id':1,'name':'老王','age':22}
student2 = student1.copy()
print(id(student1))
print(id(student2))

print(student1)
print(student2)

student1['id']=110

print(student1)
print(student2)

print('*'*40)

d1 = dict.fromkeys(['1','2','3'],'老王')
print(d1)


print('*'*40)
student = {'id':1,'name':'老王','age':22}
print(student.setdefault('id'))
print(student)
print(student.setdefault('num',110))
print(student)

print('*'*40)
student1 = {'id':1,'name':'老王','age':22}
student2 = {'score':1}
student2.update(student1)
print(student1)
print(student2)
