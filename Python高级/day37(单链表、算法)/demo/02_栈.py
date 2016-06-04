"""
Stack() 创建一个新的空栈
push(item) 添加一个新的元素item到栈顶
pop() 弹出栈顶元素
peek() 返回栈顶元素
is_empty() 判断栈是否为空
size() 返回栈的元素个数
"""

class Stack(object):
    def __init__(self):
        self.__items = []
    def push(self,item):
        self.__items.append(item)
    def pop(self):
        return self.__items.pop()
    def peek(self):
        return self.__items[len(self.__items)-1]
    def is_empty(self):
        return len(self.__items)==0
    def size(self):
        return len(self.__items)


if __name__ == '__main__':
    myStack = Stack()
    myStack.push(1)
    myStack.push(2)
    myStack.push(3)
    print(myStack.pop())
    print(myStack.pop())
    print(myStack.peek())

