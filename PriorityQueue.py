class priorityQueue:
	def __init__(self):
		# Initialize a list of maxSize and keep a variable storing the position of the heap's last element.
		# Yes I'm using a list like an array, Probably not the most pythonic way of doing this.
		self.size = 0
		self.heap = [0]*10
	
	# Function to compare the size of two elements in the array.
	def less(self, n1, n2):
		return self.heap[n1] < self.heap[n2]	
	
	# Function to exchange the contents of two positions in the array.
	def exchange(self, n1, n2):
		temp = self.heap[n1]
		self.heap[n1] = self.heap[n2]
		self.heap[n2] = temp
	
	# Function that swaps an element with it's parent until it's parent is greater than the element.
	def swim(self, k):
		while k > 1 and self.less(k//2, k):
			self.exchange(k//2, k)
			k = k//2

	# Function that sinks an element down until it's children are smaller than it.
	def sink(self, k):
		while k*2 < self.size:
			largestChild = k*2
			if self.less(k*2, (k*2)+1):
				largestChild += 1
			if self.less(k, largestChild):
				self.exchange(largestChild, k)
			else:
				break
			k = largestChild

	# Function to insert an element
	def insert(self, item):
		self.size += 1
		self.heap[self.size] = item
		self.swim(self.size)

	# Function to get the max element.
	def popMax(self):
		if self.size == 0:
			return None
		top = self.heap[1]
		self.heap[1] = self.heap[self.size]
		self.size -= 1
		self.sink(1)
		return top

newPQ = priorityQueue()

print("Testing priority queue")
assert newPQ.popMax() == None, "Popping empty queue did not return None"
newPQ.insert(5)
newPQ.insert(3)
newPQ.insert(10)
newPQ.insert(9)
assert newPQ.popMax() == 10, "First pop should be 10"
assert newPQ.popMax() == 9, "Second pop should be 9"
assert newPQ.popMax() == 5, "Third pop should be 5"
assert newPQ.popMax() == 3, "Last pop should be 3"
print("All tests passed.")
