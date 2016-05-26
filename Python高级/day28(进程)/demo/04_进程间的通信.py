from multiprocessing import  Queue

myQ = Queue(4)

myQ.put('msg1')
myQ.put('msg2')
myQ.put('msg3')
myQ.put('msg4')



