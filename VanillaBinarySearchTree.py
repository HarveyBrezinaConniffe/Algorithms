class BSTNode:
	def __init__(self, key, value, left, right):
		self.key = key
		self.value = value
		self.left = left
		self.right = right

class VanillaBST:
	def __init__(self):
		self.root = None
	
	def insert(self, key, value):
		node = BSTNode(key, value, None, None)
		if self.root == None:
			self.root = node
		else:
			parent = None
			current = self.root
			while current != None:
				parent = current
				if node.key < current.key:
					current = current.left
				elif node.key > current.key:
					current = current.right
				elif node.key == current.key:
					return -1
			if node.key > parent.key:
				parent.right = node
			elif node.key < parent.key:
				parent.left = node
			return 0
	
	def search(self, key):
		current = self.root
		while current != None:
			if current.key == key:
				return current.value
			elif key < current.key:
				current = current.left
			elif key > current.key:
				current = current.right
		return None
		
	def delete(self, key):
		current = self.root
		while current != None:
			if current.key == key:
				return current.value
			elif key < current.key:
				current = current.left
			elif key > current.key:
				current = current.right
		return -1

searchTree = VanillaBST()

print("Testing BST")

searchTree.insert(20, "Test1")
searchTree.insert(17, "Test2")
searchTree.insert(24, "Test3")

assert searchTree.search(20) == "Test1"
assert searchTree.search(17) == "Test2"
assert searchTree.search(24) == "Test3"

print("All tests passed!")
