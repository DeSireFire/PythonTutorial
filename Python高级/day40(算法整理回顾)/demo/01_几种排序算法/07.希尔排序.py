import time,random

#source = [8, 6, 4, 9, 7, 3, 2, -4, 0, -100, 99]
source = [92, 77, 8,67, 6, 84, 55, 85, 43, 67]

#source = [ random.randrange(10000+i) for i in range(10000)]

step = int(len(source)/2) #分组步长

t_start = time.time()

while step >0:
    print("---step ---", step)
    #对分组数据进行插入排序
    for index in range(0,len(source)):
        if index + step < len(source):
            current_val = source[index] #先记下来每次大循环走到的第几个元素的值
            if current_val > source[index+step]: #switch
                source[index], source[index+step] = source[index+step], source[index]
    step = int(step/2)
else: #把基本排序好的数据再进行一次插入排序就好了
    for index in range(1, len(source)):
        current_val = source[index]  # 先记下来每次大循环走到的第几个元素的值
        position = index

        while position > 0 and source[
                    position - 1] > current_val:  # 当前元素的左边的紧靠的元素比它大,要把左边的元素一个一个的往右移一位,给当前这个值插入到左边挪一个位置出来
            source[position] = source[position - 1]  # 把左边的一个元素往右移一位
            position -= 1  # 只一次左移只能把当前元素一个位置 ,还得继续左移只到此元素放到排序好的列表的适当位置 为止

        source[position] = current_val  # 已经找到了左边排序好的列表里不小于current_val的元素的位置,把current_val放在这里
    print(source)

t_end = time.time() 
host = t_end - t_start

print("cost:",host)
