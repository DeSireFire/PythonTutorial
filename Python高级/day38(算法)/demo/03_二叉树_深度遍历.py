class MyQueue(object):
    """队列"""
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        """出队列"""
        return self.items.pop()

    def size(self):
        """返回大小"""
        return len(self.items)

class MyNode(object):
    """节点"""
    def __init__(self,item,lchild=None,rchild=None):
        self.item = item
        self.lchild = lchild
        self.rchild = rchild

class MyTree(object):
    """二叉树"""
    def __init__(self, item=None):
        node = None
        if item:
            node = MyNode(item)
        self.__root = node

    def add(self,item):
        """新增"""

        myNode = MyNode(item)

        if self.__root==None:
            self.__root = myNode
            return


        myQueue = MyQueue()                 #创建新的队列：先进先出
        myQueue.enqueue(self.__root)        #放入根节点
        while myQueue.size():               #循环
            cur = myQueue.dequeue()         #出队列
            if cur.lchild == None:          #左孩子是否为None
                cur.lchild = myNode
                return
            elif cur.rchild == None:
                cur.rchild = myNode
                return
            else:
                myQueue.enqueue(cur.lchild)
                myQueue.enqueue(cur.rchild)




    def pre_travel(self,root):
        if root==None:
            return
        print(root.item,end='\t')
        self.pre_travel(root.lchild)
        self.pre_travel(root.rchild)

    def mid_travel(self, root):
        if root == None:
            return
        self.mid_travel(root.lchild)
        print(root.item, end='\t')
        self.mid_travel(root.rchild)

    def last_travel(self, root):
        if root == None:
            return
        self.last_travel(root.lchild)
        self.last_travel(root.rchild)
        print(root.item, end='\t')

    def getRoot(self):
        return self.__root



if __name__ == '__main__':
    myTree = MyTree()
    myTree.add(0)
    myTree.add(1)
    myTree.add(2)
    myTree.add(3)
    myTree.add(4)
    myTree.add(5)
    myTree.add(6)
    myTree.add(7)
    myTree.add(8)
    myTree.add(9)

    myTree.pre_travel(myTree.getRoot())

    print('')

    myTree.mid_travel(myTree.getRoot())

    print('')

    myTree.last_travel(myTree.getRoot())