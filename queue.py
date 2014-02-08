class QueueStack (object):
	def __init__(self):
		stack1 = []
		stack2 = []

	def put(self, obj):
		stack1.append(obj)

	def get(self, obj):
		if not stack2:
			self.fillStack2()
			
		return stack2.pop()

	def fillStack2(self):
		while stack1:
			stack2.append(stack1.pop)

	def peek(self):
		if not stack2:
			return stack1[0]
		else:
			return stack2[-1]

	def isEmpty(self):
		if stack1 or stack2:
			return False
		return True

q = QueueStack()

for i in range(5):
	q.put(i)

while not q.isEmpty():
	print q.get