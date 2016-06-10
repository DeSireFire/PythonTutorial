class Node(object):
	"""docstring for SinCycLinkedList"""
	#初始化节点
	def __init__(self,item):
		self.item = item
		self.next = None

class SinCycLinkedList(object):
	"""docstring for SinCycLinkedList"""
	def __init__(self):
		self._head = None
		
	# is_empty() 判断链表是否为空
	def is_empty(self):
		return self._head == None

	# length() 返回链表的长度
	def length(self):
		if self.is_empty():
			return 0
		count = 1
		cur = self._head
		while cur.next != self._head:
			count += 1
			cur = cur.next
		return count
	# travel() 遍历
	def travel(self):
		if self.is_empty():
			return
		cur = self._head
		print(cur.item)
		while cur.next != self._head:
			cur = cur.next
			print(cur.item)
		print("")
	# add(item) 在头部添加一个节点
	def add(self,item):
		node = Node(item)
		if self.is_empty():
			self._head = node
			node.next = self._head
		else:
			node.next = self._head
			cur = self._head
			while cur.next != self._head:
				cur = cur.next
			cur.next = node
			self._head = node
	# append(item) 在尾部添加一个节点
	def append(self,item):
		node = Node(item)
		if self.is_empty():
			self._head = node
			node.next = self._head
		else:
			cur = self._head
			while cur.next != self._head:
				cur = cur.next
			cur.next = node#将尾节点指向node
			node.next = self._head#将node指向头结点_head
	# insert(pos, item) 在指定位置pos添加节点
	def insert(self,pos,item):
		if pos <= 0:
			self.add(item)
		elif pos > (self.length()-1):
			self.append(item)
		else:
			node = Node(item)
			cur = self._head
			count = 0
			while count < (pos-1):
				count += 1
				cur = cur.next
			node.next = cur.next
			cur.next = node
	# remove(item) 删除一个节点
	def remove(self,item):
		if self.is_empty():
			return
		cur = self._head
		pre = None
		if cur.item == item:
			#如果不止一个节点
			if cur.next != self._head:
				#先找到尾节点，将尾节点的next指向第二个节点
				while cur.next != self._head:
					cur = cur.next
				cur.next = self._head.next
				self._head = self._head.next
			else:
				#链表只有一个节点
				self._head = None
		else:
			pre = self._head
			while cur.next != self._head:
				if cur.item == item:
					pre.next = cur.next
					return
				else:
					pre = cur
					cur = cur.next
			if cur.next == item:
				pre.next = cur.next
	# search(item) 查找节点是否存在
	def search(self,item):
		if self.is_empty():
			return False
		cur = self._head
		if cur.item == item:
			return True
		while cur.next != self._head:
			cur = cur.next
			if cur.item == item:
				return True
		return False


def main():
	ll = SinCycLinkedList()
	ll.add(1)
	ll.add(2)
	ll.append(3)
	ll.insert(2, 4)
	ll.insert(4, 5)
	ll.insert(0, 6)
	print("length:",ll.length())
	ll.travel()
	print(ll.search(3))
	print(ll.search(7))
	ll.remove(1)
	print("length:",ll.length())
	ll.travel()

if __name__ == "__main__":
	main()