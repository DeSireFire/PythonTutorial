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

	def preorder(self,root):
		if root == None:
			return
		print(root.item,end="\t")
		self.preorder(root.lchild)
		self.preorder(root.rchild)

	def inorder(self,root):
		if root == None:
			return
		self.inorder(root.lchild)
		print(root.item,end="\t")
		self.inorder(root.rchild)

	def postorder(self,root):
		if root == None:
			return
		self.postorder(root.lchild)
		self.postorder(root.rchild)
		print(root.item,end="\t")

if __name__ == '__main__':
	mytree = MyTree()
	mytree.add(0)
	mytree.add(1)
	mytree.add(2)
	mytree.add(3)
	mytree.add(4)
	mytree.add(5)
	mytree.add(6)
	mytree.add(7)
	mytree.add(8)
	mytree.add(9)

	mytree.preorder(mytree.root)
	print()
	mytree.inorder(mytree.root)
	print()
	mytree.postorder(mytree.root)
	print()