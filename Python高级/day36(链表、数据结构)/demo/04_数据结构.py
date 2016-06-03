# 保存咱班所有人的信息,并要快速的获取

ls=[
    ('秦佳','男',22,175),
    ('阎旺','男',25,185)
]

print(ls[0][0])


dic={
    '秦佳':('男',22,175),
    '阎旺':('男',22,175)
}

print(dic['秦佳'])


#对时间定义数据结构

# ADT mydate{
#     数据（年月日十分秒...）
#     操作
#         1 获取年
#         2 设置年
#         ...
# }end mydate

class mydate:
    # 数据（年月日十分秒）
    def __init__(self, year, month):
        pass

    # 操作
    def getYear(self):
        pass


class MyDate:
    # 数据（年月日十分秒）
    def __init__(self,year,month):
        self.year = year
        self.month = month
    #操作
    def getYear(self):
        return  self.year
