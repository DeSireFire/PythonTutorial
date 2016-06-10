from time import sleep
from multiprocessing import Process
from random import random

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