import Queue

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def insert(self, data):
        if data < self.data:
            if self.left == None:
                self.left = Node(data)
            else:
                self.left.insert(data)
        else:
            if self.right == None:
                self.right = Node(data)
            else:
                self.right.insert(data)

    def find(self, data, parent=None):
        if data == self.data:
            return self, parent
        
        if data < self.data:
            if self.left == None:
                return None, parent
            else:
                return self.left.find(data, self)
        else:
            if self.right == None:
                return None, parent
            else:
                return self.right.find(data, self)
    
    def delete(self, data):
        node, parent = self.find(data)
        if not node == None:
            numChildren = node.numberOfChildren()
            if numChildren == 0:
                if parent.left is node:
                    parent.left = None
                else:
                    parent.right = None
                del node
            elif numChildren == 1:
                if node.left:
                    n = node.left
                else:
                    n = node.right
                if parent.left is node:
                    parent.left = n
                else:
                    parent.right = n
                del node
            else:
                parent = node
                successor = parent.right
                while successor.left:
                    succesor = sucessor.left
                    node = successor
                parent.data = successor.data
                if successor.right:
                    node.left = successor.right
                del successor
                
    
    def numberOfChildren(self):
        if self.left == None:
            if self.right == None:
                return 0
            else:
                return 1
        else:
            if self.right == None:
                return 1
            else:
                return 2
    
    def printInOrder(self):
        if self.left:
            self.left.printInOrder()
        print self.data
        if self.right:
            self.right.printInOrder()
    
    def printPreOrder(self):
        print self.data
        if self.left:
            self.left.printPreOrder()
        if self.right:
            self.right.printPreOrder()
    
    def printPostOrder(self):
        if self.left:
            self.left.printPostOrder()
        if self.right:
            self.right.printPostOrder()
        print self.data
    
    def printBreadthFirst(self):
        q = Queue.Queue()
        
        q.put(self)  
        
        while not q.empty():
            node = q.get()
            print node.data
            if node.left:
                q.put(node.left)
            if node.right:
                q.put(node.right)
        
    
root = Node(8)
    
root.insert(11)
root.insert(6)
root.insert(9)
root.insert(3)
root.insert(10)
root.insert(7)
root.insert(13)

node, parent = root.find(10)

root.delete(10)
root.printInOrder()
print 'Pre Order'
root.printPreOrder()
print 'Post Order'
root.printPostOrder()
print 'Breadth First'
root.printBreadthFirst()


