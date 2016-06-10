class MyDueue(object):
	"""docstring for MyQueue"""
	# Deque() 创建一个空的双端队列
	def __init__(self):
		self.item = []

	# add_front(item) 从队头加入一个item元素
	def add_front(self,item):
		self.item.insert(0,item)

	#add_rear(item) 从队尾加入一个item元素
	def add_rear(self,item):
		self.item.append(item)

	# remove_front() 从队头删除一个item元素
	def remove_front(self):
		return self.item.pop(0)

	# remove_rear() 从队尾删除一个item元素
	def remove_rear(self):
		return self.item.pop()

	# is_empty() 判断一个队列是否为空
	def is_empty(self):
		return self.item == []

	# size() 返回队列的大小	
	def size(self):
		return len(self.item)

if __name__ == "__main__":

	due = MyDueue()
	due.add_front(5)
	due.add_front(6)
	due.add_rear(8)
	print(due.is_empty())
	print(due.size())
	print(due.remove_front())
	print(due.remove_rear())
	print(due.is_empty())
	print(due.size())