import random
'''
break可以用来结束整个循环。
continue可以结束本次循环，进入下一次循环。

注意：

break/continue只能用在循环中，除此以外不能单独使用。
break/continue在嵌套循环中，只对最近的一层循环起作用。

'''
play = 'True'
while play == 'True':
    for i in range(3):
        rec = None
        num = 3
        com = random.randint(0,2)

        players = input('输入：(剪刀 石头 布):')

        mylist = ('剪刀',"石头",'布','True','False')

        if players not in mylist:
            print('输入的东西不太对！')
        else:
            print('你：%s 它：%s'%(players,mylist[com]))
            if players == mylist[com]:
                rec == 'Lose!'
                print('平手呢！')
            else:
                    if players == '剪刀' and mylist[com] == '石头':
                        rec = 'Lose!'
                        print('Lose!')
                    elif players == '布' and mylist[com] == '剪刀':
                        rec = 'Lose!'
                        print('Lose!')
                    elif players == '石头' and mylist[com] == '布':
                        rec = 'Lose!'
                        print('Lose!')
                    elif players == '石头' and mylist[com] == '剪刀':
                        rec = 'Win!'
                        print('Win!')
                    elif players == '布' and mylist[com] == '石头':
                        rec = 'Win!'
                        print('Win!')
                    elif players == '剪刀' and mylist[com] == '布':
                        rec = 'Win!'
                        print('Win!')
        if rec == 'Lose!' :
            num -= 1
            print('还有%s次机会'%num)
        else:
            break

    QA = str(input('是否继续游戏？（True or False）:'))
    play = QA

