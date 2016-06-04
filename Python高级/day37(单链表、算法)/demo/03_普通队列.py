class MyQueue(object):
    """队列"""
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        """进队列"""
        #self.items.append(item)
        self.items.insert(0,item)

    def dequeue(self):
        """出队列"""
        #return self.items.pop(0)
        return self.items.pop()

    def size(self):
        """返回大小"""
        return len(self.items)



if __name__ == '__main__':
   myQueue = MyQueue()
   myQueue.enqueue(1)
   myQueue.enqueue(2)
   myQueue.enqueue(3)
   print(myQueue.dequeue())
   print(myQueue.dequeue())
   print(myQueue.dequeue())

