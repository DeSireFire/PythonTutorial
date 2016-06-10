class Node(object):
	"""docstring for Node"""
	def __init__(self,item):
		self.item = item
		self.next = None
		self.prev = None

class DLinkList(object):
	"""docstring for DLinkList"""
	def __init__(self):
		self._head = None
		
	# is_empty() 链表是否为空
	def is_empty(self):
		return self._head == None

	# length() 链表长度
	def length(self):
		cur = self._head
		count = 0
		while cur != None:
			count += 1
			cur = cur.next
		return count

	# travel() 遍历链表
	def travel(self):
		cur = self._head
		while cur != None:
			print(cur.item)
			cur = cur.next
		print()

	# add(item) 链表头部添加
	def add(self,item):
		node = Node(item)
		if self.is_empty():
			self._head = node
		else:
			node.next = self._head
			self._head.prev = node
			self._head = node

	# append(item) 链表尾部添加
	def append(self,item):
		node = Node(item)
		if self.is_empty():
			self._head = node
		else:
			cur = self._head
			while cur.next != None:
				cur = cur.next
			cur.next = node
			node.prev = cur

	# insert(pos, item) 指定位置添加
	def insert(self,pos,item):
		if pos <= 0:
			self.add(item)
		elif pos > (self.length()-1):
			self.append(item)
		else:
			node = Node(item)
			cur = self._head
			count = 0
			while count <(pos-1):
				count += 1
				cur = cur.next
			node.prev = cur
			node.next = cur.next
			cur.next.prev = node
			cur.next = node

	# remove(item) 删除节点
	def remove(self,item):
		if self.is_empty():
			return
		else:
			cur = self._head
			if cur.item == item:
				if cur.next == None:
					self._head = None
				else:
					cur.next.prev = None
					self._head = cur.next
				return
			while cur != None:
				if cur.item == item:
					cur.prev.next = cur.next
					cur.next.prev = cur.prev
					break
				cur = cur.next
	# search(item) 查找节点是否存在
	def search(self,item):
		cur = self._head
		while cur != None:
			if cur.item == item:
				return True
			cur = cur.next
		return False

def main():
	ll = DLinkList()
	ll.add(1)
	ll.add(2)
	ll.append(3)
	ll.insert(2, 4)
	ll.insert(4, 5)
	ll.insert(0, 6)
	print("length:",ll.length())
	ll.travel()
	print(ll.search(3))
	print(ll.search(4))
	ll.remove(1)
	print("length:",ll.length())
	ll.travel()

if __name__ == '__main__':
	main()