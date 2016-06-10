#单链表的实现
class SingleLinkList(object):

	def __init__(self):
		self._head = None
	
	"""判断链表是否为空"""
	def is_empty(self):
		return self._head == None
	"""链表长度"""
	def length(self):
		tou = self._head
		count = 0
		while tou != None:
			count+=1
			tou = tou.next
		return count
	"""遍历链表"""
	def travel(self):
		tou = self._head
		while tou != None:
			print(tou.item,"\t",end=" ")
			tou = tou.next
		print("")
	"""头部添加元素"""
	def add(self,item):
		#先创建一个保存值的节点
		node = SigleNode(item)
		node.next = self._head
		self._head = node
	"""尾部添加元素"""
	def append(self,item):
		node = SigleNode(item)
		if(self._head == None):
			self._head = node
		else:
			tou = self._head
			while tou.next != None:
				tou = tou.next
			tou.next = node
	"""指定位置添加元素"""
	def insert(self,addr,item):

		if addr <= 0:
			self.add(item)
		elif addr > (self.length()-1):
			self.append(item)
		else:
			node = SigleNode(item)
			count = 0
			pre = self._head
			while count < (addr-1):
				count += 1
				pre = pre.next
			node.next = pre.next
			pre.next = node
	#删除节点"""
	def remove(self,item):
	 	tou = self._head
	 	pre = None
	 	while  tou != None:
	 		if tou.item == item:
	 			if not pre:
	 				self._head = node.next
	 			else:
	 				pre.next = tou.next
	 			break
	 		else:
	 			pre = tou
	 			tou = tou.next
	"""链表查找节点是否存在，并返回True或者False"""
	def search(self,item):
	 	tou = self._head
	 	while tou != None:
	 		if tou.item == item:
	 			return True
	 		tou = tou.next
	 	return False

#节点的实现
class SigleNode(object):
	
	def __init__(self,item):
		self.item = item
		self.next = None

def main():
	ll = SingleLinkList()
	ll.add(1)
	ll.add(2)
	ll.append(3)
	ll.insert(2, 4)
	print("长度:",ll.length())
	ll.travel()
	print(ll.search(3))
	print(ll.search(5))
	ll.remove(1)
	print("长度:",ll.length())
	ll.travel()

if __name__ == '__main__':
	main()


'''
ADT的抽象实现
'''
class SingleLinkList(object):
    def __init__(self, node):
        pass

    def is_empty(self):
        pass

    def length(self):
        pass
    def travel(self):
        pass
    def add(self):
        pass
    def append(self):
        pass
    def insert(self):
        pass
    def remove(self):
        pass
    def search(self):
        pass



class Node(object):
    """节点"""
    def __init__(self, elem):
        """初始化
            elem：当前节点的值
            next：当前节点的下个节点的引用
        """
        self.elem = elem
        self.next = None




class SingleLinkList(object):
    """单链表
        扩展：可以传递一个可迭代的对象，当做初始值
    """
    def __init__(self, elem=None):
        node = None
        if elem:
            node = Node(elem)
        self.__head = node

    def is_empty(self):
        """链表是否为空"""
        return self.__head == None

    def length(self):
        """链表长度"""
        # cur游标，用来移动遍历节点
        cur = self.__head
        # count记录数量
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """遍历整个链表"""
        cur = self.__head
        while cur != None:
            print(cur.elem, end="\t")
            cur = cur.next

    def add(self, item):
        """链表头部添加元素，头插法"""
        node = Node(item)
        node.next = self.__head
        self.__head = node

    def append(self, item):
        """链表尾部添加元素, 尾插法"""
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next != None:
                cur = cur.next
            cur.next = node

    def insert(self, pos, item):
        """指定位置添加元素
        :param  pos 从0开始
        """
        if pos <= 0:
            self.add(item)
        elif pos > (self.length()-1):
            self.append(item)
        else:
            pre = self.__head
            count = 0
            while count < (pos-1):
                count += 1
                pre = pre.next
            # 当循环退出后，pre指向pos-1位置
            node = Node(item)
            node.next = pre.next
            pre.next = node

    def remove(self, item):
        """删除节点"""
        cur = self.__head
        pre = None
        while cur != None:
            if cur.elem == item:
                # 先判断此结点是否是头节点
                # 头节点
                if cur == self.__head:
                    self.__head = cur.next
                else:
                    pre.next = cur.next
                break
            else:
                pre = cur
                cur = cur.next

    def search(self, item):
        """查找节点是否存在"""
        cur = self.__head
        while cur != None:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        return False

    def index(self, index):
        """根据下标查找节点的值,"""

        if index>=self.length():
            raise IndexError('下标越界')
        elif index<0:
            raise IndexError('下标越界')
        else:
            count = 0
            cur = self.__head
            while count < index:
                count += 1
                cur = cur.next
            return cur.elem


if __name__ == "__main__":
    ll = SingleLinkList()
    print(ll.is_empty())
    print(ll.length())

    ll.append(1)
    print(ll.is_empty())
    print(ll.length())


    ll.append(2)
    ll.add(8)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.append(6)
    # 8 1 2 3 4 5 6
    ll.insert(-1, 9) # 9 8 1 23456
    ll.travel()
    ll.insert(3, 100) # 9 8 1 100 2 3456
    ll.travel()
    ll.insert(10, 200) # 9 8 1 100 23456 200
    ll.travel()
    ll.remove(100)
    ll.travel()
    ll.remove(9)
    ll.travel()
    ll.remove(200)
    ll.travel()
