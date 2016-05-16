'''
ls = [1,3,4,5,6,7,3,3,3,4]
n = len(ls) 
m = 1
names=[]
while m<n:
	if ls[m]==3:
		names.append(m)
	m+=1
print(names)
'''

listA = [1,2,2,3,4,5,2,6,7]
while listA.count(2)>0:
	print(listA.index(2))
	listA[listA.index(2)] = 0
