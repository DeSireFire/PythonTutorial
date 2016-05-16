'''
__del__()

在对象被删除的时候会自动调用
开发中一般也不用


__del__这个方法，如果没有定义。系统在运行过程中，
当释放内存资源的时候，系统会加上这个方法，调用，执行里面的代码，来释放资源。


一旦自己写这个方法了，系统就不会自动添加了，垃圾回收机制在回收的时候，占用的资源可能不会被释放了。

垃圾回收机制，是自动的。不需要程序员关注。


小整数（字符串）常量池


使用del在删除对象的时候，其实并不一定删除引用的对象
只是删除，这个引用而已。引用计数减1
当引用计数为0的时候（__del__魔法方法被调用），这个对象就是垃圾。
垃圾回收机制，在执行的时候，会清除这个垃圾。


del xxx 不会主动调用__del__方法，只有引用计数==0时，__del__()才会被执行，
并且定义了__del_()的实例无法被Python的循环垃圾收集器收集，所以尽量不要自定义__del__()。
一般情况下，__del__() 不会破坏垃圾处理器。
'''

class Dog:
	def __del__(self):
		print('del...')
		#释放资源


wangcai = Dog()
xiaoqiang = wangcai


import sys

del xiaoqiang
num = sys.getrefcount(wangcai)-1
print(num)

import time
print('休眠3秒中。。。')
time.sleep(3)


del wangcai

print('休眠3秒中。。。')
time.sleep(3)


 
