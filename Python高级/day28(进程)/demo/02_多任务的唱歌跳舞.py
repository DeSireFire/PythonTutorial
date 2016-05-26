from time import sleep
from multiprocessing import  Process
from random import  random


def sing():
    for i in range(3):
        print("正在唱歌...%d" % i)
        sleep(random())


def dance():
    for i in range(3):
        print("正在跳舞...%d" % i)
        sleep(random())

class MyProcess1(Process):
    def run(self):
        self.__dance()

    def __dance(self):
        for i in range(3):
            print("正在跳舞...%d" % i)
            sleep(random())

class MyProcess2(Process):
    def run(self):
        self.__sing()

    def __sing(self):
        for i in range(3):
            print("正在唱歌...%d" % i)
            sleep(random())

















def test1():
    p1 = Process(target=sing)
    p2 = Process(target=dance)

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print('game over...')


def test2():
    p1 = MyProcess1()
    p2 = MyProcess2()

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print('game over...')


if __name__ == '__main__':
    # test1()
    test2()