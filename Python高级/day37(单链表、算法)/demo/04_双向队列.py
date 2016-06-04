class MyQueue(object):
    """队列"""
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue_front(self, item):
        """进队列"""
        #self.items.append(item)
        self.items.insert(0,item)

    def dequeue_front(self):
        """出队列"""
        #return self.items.pop(0)
        return self.items.pop()

    def enqueue_last(self, item):
        """进队列"""
        self.items.append(item)


    def dequeue_last(self):
        """出队列"""
        return self.items.pop(0)


    def size(self):
        """返回大小"""
        return len(self.items)



if __name__ == '__main__':
   myQueue = MyQueue()
   myQueue.enqueue_front(1)
   myQueue.enqueue_front(2)
   myQueue.enqueue_front(3)
   print(myQueue.dequeue_last())

   # print(myQueue.dequeue_front())
   # print(myQueue.dequeue_front())
   # print(myQueue.dequeue_front())



   # myQueue2 = MyQueue()
   # myQueue2.enqueue_last(4)
   # myQueue2.enqueue_last(5)
   # myQueue2.enqueue_last(6)
   # print(myQueue2.dequeue_last())
   # print(myQueue2.dequeue_last())
   # print(myQueue2.dequeue_last())

