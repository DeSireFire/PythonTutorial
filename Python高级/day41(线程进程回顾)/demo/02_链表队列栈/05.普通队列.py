class MyQueue(object):
	"""docstring for MyQueue"""
	# Queue() 创建一个空的队列
	def __init__(self):
		self.item = []

	# enqueue(item) 往队列中添加一个item元素
	def enqueue(self,item):
		self.item.insert(0,item)

	# dequeue() 从队列头部删除一个元素
	def dequeue(self):
		return self.item.pop()

	# is_empty() 判断一个队列是否为空
	def is_empty(self):
		return self.item == []

	# size() 返回队列的大小	
	def size(self):
		return len(self.item)

if __name__ == "__main__":

	que = MyQueue()
	que.enqueue(2)
	que.enqueue(5)
	que.enqueue(8)
	print(que.size())
	print(que.is_empty())
	print(que.dequeue())
	print(que.dequeue())
	print(que.dequeue())


