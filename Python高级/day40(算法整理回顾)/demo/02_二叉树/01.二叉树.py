class MyQueue(object):
	"""队列MyQueue"""
	def __init__(self):
		self.item = []

	def is_empty(self):
		return self.item == []

	def enqueue(self,item):
		self.item.insert(0,item)

	def dequeue(self):
		return self.item.pop()

	def size(self):
		return len(self.item)
		
class MyNode(object):
	"""创建节点MyNode"""
	def __init__(self, item = -1,lchild = None,rchild = None):
		self.item = item
		self.lchild = lchild
		self.rchild = rchild

class MyTree(object):
	"""创建树类MyTree"""
	def __init__(self, item = None):
		node = None
		if item:
			node = MyNode(item)
		self.root = node

	#添加节点
	def add(self,item):

		mynode = MyNode(item)

		if self.root == None:
			self.root = mynode
			return
		myqueue = MyQueue()
		myqueue.enqueue(self.root)#根进入队列

		while myqueue.size():

			cur = myqueue.dequeue()

			if cur.lchild == None:
				cur.lchild = mynode
				return
			if cur.rchild == None:
				cur.rchild = mynode
				return
			else:
				myqueue.enqueue(cur.lchild)
				myqueue.enqueue(cur.rchild)
	def travel(self):
		myqueue = MyQueue()
		myqueue.enqueue(self.root)
		while myqueue.size():
			cur = myqueue.dequeue()
			print(cur.item)
			if cur.lchild != None:
				myqueue.enqueue(cur.lchild)
			if cur.rchild != None:
				myqueue.enqueue(cur.rchild)

if __name__ == '__main__':
	mytree = MyTree()
	mytree.add(1)
	mytree.add(5)
	mytree.add(8)

	mytree.travel()