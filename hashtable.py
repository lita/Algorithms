# Easy
class HashTableEasy(object):
	def __init__(self):
		self.hashtable = {}

	def add_key_value_pair(key, value):
		self.hashtable[key] = value

	def get_value(key):
		return self.hashtable[key] 

	def remove_key(key):
		self.hashtable.pop(key)

class HashTable(object):
	def __init__(self, size):
		self.items = [None]*size

	def getIndex(self, key):
		hashValue = hash(key)
		index = hashValue % len(self.items)
		return index

	def add_key_value_pair(self, key, value):
		index = self.getIndex(key)
		if not self.items[index]:
			self.items[index] = [(key, value)]
		else:
			self.items[index].append((key,value))

	def get_value(self, key):
		index = self.getIndex(key)
		items = self.items[index]
		for i in items:
			if i[0] == key:
				return value

		raise KeyError("Value doesn't exist with Key")

def main():
	myHashTable = HashTable()
	myHashTable.add_key_value_pair(10,'doggie')
	assert(myHashTable.get_value(10)=='doggie')
