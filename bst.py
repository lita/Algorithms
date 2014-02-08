class Node(object):
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value
        

class BST(object):
    def __init__(self):
        self.root = None
    
    def insert(self, value):

    def _insertHelper(self, node, value):
        if node == None:
            return Node(value)
        
        if node.value < value:
            self._insertHelper(node.right, value)