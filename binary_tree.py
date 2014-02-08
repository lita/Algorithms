"""
given two nodes of a binary tree, find number of nodes on the path between the 
two nodes.
"""

class BinaryTree(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def printNode(root):
    """Prints inorder"""
    if root.left:
        printNode(root.left)
    print root.value
    if root.right:
        printNode(root.right)

def initalize():
    node = BinaryTree(4)
    node2 = BinaryTree(5)
    node = BinaryTree(2, node, node2)
    node2 = BinaryTree(1, node, BinaryTree(3))
    node = BinaryTree(10, BinaryTree(9), BinaryTree(11))
    root = BinaryTree(50, node, node2)
    return root

def countPathToNodes(root, a, b):
    results = _countPathToNodes(root, a, b)
    if results[1]:
        return results[0]
    else:
        # Did not find both items
        return None

def _countPathToNodes(node, a, b):
    found = False
    result = 0
    if node.value == a or node.value == b:
        found = True
        result = 1

    
    resultLeft = 0
    resultRight = 0
    foundLeft = False
    foundRight = False
    if node.left:
        resultLeft, foundLeft = _countPathToNodes(node.left, a, b)

    if node.right:
        resultRight, foundRight = _countPathToNodes(node.right, a, b)

    if resultRight and resultLeft:
        # we found the complete path
        return (1 + resultLeft + resultRight, True)

    if foundLeft:
        return (resultLeft, True)

    if foundRight:
        return (resultRight, True)

    if resultLeft:
        return (1+resultLeft, found)

    if resultRight:
        return (1+resultRight, found)

    return (result, False)

root = initalize()
printNode(root)
print ''
print countPathToNodes(root, 5, 2)