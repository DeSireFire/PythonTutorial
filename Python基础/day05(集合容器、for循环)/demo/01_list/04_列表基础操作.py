list = [1,2,3,4,5]
# 按下标取值1
print(list[0])
# 按下标最后一个元素
print(list[-1])

search  = list.index(5)
#查找对应值的下标
print(search)

list = [1,2,3,4,5,5,5]
#查找某个元素的出现次数
mynum = list.count(5)
print(mynum)

#列表长度
print(len(list))

#大小值
print(max(list))
print(min(list))

#末尾添加
list.append(8)
print(list)

#从下标插入
list.insert(0,9)
print(list)

#追加多个值
list2 = [233,666,888]
list.extend(list2)
print(list)


# 区别
list.append(list2)
print(list)

# 从下标修改对应元素
list[0] = 0
print(list)

# 弹出
rec = list.pop()
print(rec)
print(list)

#按下标弹出
rec = list.pop(0)
print(rec)
print(list)

#按下标删除
list.pop(4)
print(list)

#按元素删除
list.remove(5)
print(list)

strlist = ['Hi~']*20
print(strlist)
print(list2+list2)
print('hello' in strlist)
print('hello' not in strlist)

# 排序
list3 = list2+list2
print(list3)
list3.sort()
print(list3)
list4 = list3.sort()
print(list4)
# 区别
list3 = list2+list2
list4 = sorted(list3)
print(list4)

# 循环判断是否为列表最后一个元素
# list5 = [1,2,3,4,5]
# while True :
#     XX = int(input("请输入一个数字："))
#     if XX == list[-1]:
#         print("True")
#     else:
#         print("False")

# 使用下标比对值
a = [1,2,3,45,56,76,87,8]
b = 8
c = a.index(b)



if len(a)-1 == c:
    print("true")
else:
    print("false")


# 按元素查询下标
list = [1,2,3,5,6,2,4,8,9,2,7]
la = list.index(2)
print(la)
# 查询元素在列表的数量
lala = list.count(2)
print(lala)
# 按下表位置插入元素（下标2，插入11）
list.insert(2,11)
print(list)
# 从末尾添加元素
list.append(678)
print(list)
# 删除并弹出末尾元素
list.pop()
print(list)
# 按下标删除元素
del list[0]
print(list)
# 函数用于在列表末尾一次性追加另一个序列中的多个值
list.extend([34,43,545,67])
print(list)
# 移除元素
list.remove(11)
print(list)
list.remove(2)
print(list)
# 集合容器嵌套取值并修改
k = ([2,3,1,3,4,5],'老王',546)
print(k)
k[0][5] = 66
print(k)
