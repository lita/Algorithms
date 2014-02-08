class Node ():
	def __init__(self, value):
	    self.value = value
	    self.next = None
	
	def printNodes(self):
	    print self.value,
	    print '->',
	    cur = self.next
	    while cur:
	        print cur.value,
	        print '->',
	        cur = cur.next


def initalize ():
    head = Node(10)
    cur = head
    for i in range(9,0, -1):
        cur.next = Node(i)
        cur = cur.next
    
    return head

def reverseLinkedList(head):
    if head == None:
        return None
    if head.next == None:
        return head
    
    reverse = reverseLinkedList(head.next)
    head.next.next = head
    head.next = None
    print reverse.value
    
    return reverse

def removeDups(head):
    duptracker = {}
    cur = head
    duptracker[cur]
    

def assignPartition(node, l):
    l.next = node
    node.next = None
    
    return node

def partitionList(head, p):
    greaterHead = greater = None
    lessHead = less = None
    equalHead = equal = None
    
    cur = head
    while cur.next:
        if p == cur.value:
            if equalHead == None:
                equalHead = cur
                equalHead = equal
            else:
                equal.next = cur
                equal = cur
        elif p > cur.value:
            if greaterHead == None:
                greaterHead = cur
                greaterHead = greater
            else:
                greater.next = cur
                greater = cur
        else:
            if lessHead == None:
                lessHead =  cur
                less = lessHead
            else:
                less.next = cur
                less = cur
        cur = cur.next
    
    newHead = lessHead
    if less:
        if equal:
            less.next = equalHead
        elif greater:
            less.next = greaterHead
    elif equal:
        newHead = equalHead
        if greater:
            equal.next = greaterHead
    else:
        newHead = greaterHead
        greater.next = None
    
    return newHead
    
head = initalize()
head.printNodes
print ""
head = partitionList(head, 5)
head.printNodes()

    