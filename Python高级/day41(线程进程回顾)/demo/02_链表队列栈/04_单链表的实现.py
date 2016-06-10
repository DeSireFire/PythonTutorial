class SigleNode():
	def __init__(self,item,next=None):
		self.item=item
		self.next=next

class SingleLinkList(object):

	def __init__(self):
		self._head = None

	def is_empty(self):#判断是否为空
		return self._head == None

	def length(self):#判断链表长度
		len = self._head
		count = 0
		#尾节点指向None时，达到末尾
		while len != None:
			count+=1
			len = len.next
		return count
		
	def travel(self):#遍历链表
		len = self._head
		while len != None:
			print(len.item,'\t',end='')
			len = len.next
		print("")
		
	def add(self,item):#头部添加元素
		node = SigleNode(item)#先创建一个保存item的节点
		node.next = self._head#将新节点的链接域next指向头结点
		self._head = node#将链表的头结点指向新的节点

	def append(self,item):#尾部添加元素
		node = SigleNode(item)
		if self.is_empty():#判断链表是否为空，或者self._head = None
			self._head = node
		else:# 若不为空，则找到尾部，将尾节点的next指向新节点
			len = self._head
			while len.next != None:
				len = len.next
			len.next = node

	def insert(self,pos,item):#指定位置添加元素
		if pos <= 0: # 若指定位置pos为第一个元素之前，则执行头部插入
			self.add(item)
		elif pos > (self.length()-1):# 若指定位置超过链表尾部，则执行尾部插入
			self.append(item)
		else: # 找到指定位置
			node = SigleNode(item)
			count = 0
			#pre用来指向指定位置pos的前一个位置pos-1，初始从头节点开始移动到指定位置
			pre = self._head
			while count < (pos-1):
				count += 1
				pre = pre.next
			 # 先将新节点node的next指向插入位置的节点
			node.next = pre.next
			 # 将插入位置的前一个节点的next指向新节点
			pre.next = node

	def remove(self,item):#删除节点
		len = self._head
		pre = None
		while len != None:
			if len.item == item:#找到指定元素
				if not pre:
					self._head = len.next#将头指针指向节点的后一个节点
				else:
					pre.next = len.next#将删除位置前一个节点的next指向删除位置的后一个节点
				break
			else:
				#继续按链表后移节点
				pre = len
				len = len.next

	def search(self,item):#链表查找节点是否存在，并返回True或者False
		len = self._head
		while len != None:
			if len.item == item:
				return True
			len = len.next
		return False

if __name__ == "__main__":
	ll = SingleLinkList()
	ll.add(1)
	ll.add(2)
	ll.append(3)
	ll.insert(2,4)
	print("length:",ll.length())
	ll.travel()

	print(ll.search(3))
	print(ll.search(5))
	ll.remove(1)
	print ("length:",ll.length())
	ll.travel()