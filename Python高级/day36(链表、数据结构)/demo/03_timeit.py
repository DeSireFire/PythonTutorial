from timeit import Timer

def test1():
   l = []
   for i in range(1001):
      l = l + [i]

def test11():
   l = []
   for i in range(1001):
      l +=[i]

def test2():
   l = []
   for i in range(1001):
      l.append(i)

def test3():
   l = [i for i in range(1001)]

def test4():
   l = list(range(1001))



myTimer1 = Timer('test1()','from __main__ import test1')
sencond1 = myTimer1.timeit(1000)
print(sencond1)
myTimer1 = Timer('test11()','from __main__ import test11')
sencond1 = myTimer1.timeit(1000)
print(sencond1)


myTimer1 = Timer('test2()','from __main__ import test2')
sencond1 = myTimer1.timeit(1000)
print(sencond1)

myTimer1 = Timer('test3()','from __main__ import test3')
sencond1 = myTimer1.timeit(1000)
print(sencond1)

myTimer1 = Timer('test4()','from __main__ import test4')
sencond1 = myTimer1.timeit(1000)
print(sencond1)



