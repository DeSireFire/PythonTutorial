import time

'''
flush:将内存的东西刷到硬盘中
'''


file  = open('laowang.html','w',encoding='utf-8')

file.write('哈哈')
#file.flush()
time.sleep(10)

file.write('hehe')

file.close()