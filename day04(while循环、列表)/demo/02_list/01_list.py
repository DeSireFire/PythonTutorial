name1 = '阎旺'
name2 = '吕金鹏'
name3 = '翟晨光'
#.......
'''
一旦需要存储的数据比较多，用单个变量来存储就麻烦。
能不能找一个容器，可以存储任意多个的值，还有对每一个数据有一个编号
这样的容器，就是今天学的集合
'''
names = ['阎旺','吕金鹏','翟晨光']
ages = [1,2,3,4,5,222,'a',None,1.1,True,[1,'a']]
#print(str(names))
print(names)
print(ages)



names = ['阎旺','吕金鹏','翟晨光']
#下标从0开始
n1 = names[0]
print(n1)
n2 = names[1]
print(n2)
n3 = names[2]
print(n3)
#len可以获取集合、字符串的长度
count = len(names)
print(count)

print('*'*30)

#循环/遍历列表
index=0
while index<len(names):
	print(names[index])
	index+=1

#下标越界：IndexError: list index out of range
#print(names[3])


#空列表 
ls = []
print(len(ls))