import random

com = random.randint(0,2)

players = input('输入：(剪刀 石头 布):')

# dicts = {1:'剪刀',2:"石头",3:'布'}

mylist = ('剪刀',"石头",'布')

if players not in mylist:
    print('输入的东西不太对！')
else:
    print('你：%s 它：%s'%(players,mylist[com]))
    if players == mylist[com]:
        print('平手呢！')
    else:
        if players == '剪刀' and mylist[com] == '石头':
            print('Lose!')
        elif players == '剪刀' and mylist[com] == '布':
            print('Win!')
        elif players == '石头' and mylist[com] == '布':
            print('Lose!')
        elif players == '石头' and mylist[com] == '剪刀':
            print('Win!')
        elif players == '布' and mylist[com] == '剪刀':
            print('Lose!')
        elif players == '布' and mylist[com] == '石头':
            print('Win!')

