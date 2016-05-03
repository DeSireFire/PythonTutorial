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
