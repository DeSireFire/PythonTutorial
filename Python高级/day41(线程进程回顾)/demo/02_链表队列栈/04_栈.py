class Stack(object):
	"""Stack() 创建一个新的空栈"""
	def __init__(self):
		self.item = []
	
	# push(item) 添加一个新的元素item到栈顶
	def push(self,item):
		self.item.append(item)

	# pop() 弹出栈顶元素
	def pop(self):
		return self.item.pop()

	# peek() 返回栈顶元素
	def peek(self):
		return self.item[len(self.item)-1]

	# is_empty() 判断栈是否为空
	def is_empty(self):
		return self.item == []

	# size() 返回栈的元素个数
	def size(self):
		return len(self.item)

if __name__ == "__main__":

	s = Stack()
	s.push(22)
	s.push(33)
	s.push(55)
	s.push(66)
	print(s.is_empty())
	print(s.size())
	print(s.pop())
	s.push(100)
	print(s.peek())
