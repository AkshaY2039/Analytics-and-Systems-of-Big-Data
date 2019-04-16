# A Python program to demonstrate common binary heap operations
# Import the heap functions from python library
from heapq import heappush, heappop, heapify
import random
# heappop - pop and return the smallest element from heap
# heappush - push the value item onto the heap, maintaining
#			 heap invarient
# heapify - transform list into heap, in place, in linear time
# A class for Min Heap
class MinHeap:
	# Constructor to initialize a heap
	def __init__(self):
		self.heap = []

	def parent(self, i):
		return (i-1)/2

	# Inserts a new key 'k'
	def insertKey(self, k):
		heappush(self.heap, k)

	# Decrease value of key at index 'i' to new_val
	# It is assumed that new_val is smaller than heap[i]
	def decreaseKey(self, i, new_val):
		self.heap[i] = new_val
		while(i != 0 and self.heap[self.parent(i)] > self.heap[i]):
			# Swap heap[i] with heap[parent(i)]
			self.heap[i] , self.heap[self.parent(i)] = (
			self.heap[self.parent(i)], self.heap[i])

	# Method to remove minium element from min heap
	def extractMin(self):
		return heappop(self.heap)

	# This functon deletes key at index i. It first reduces
	# value to minus infinite and then calls extractMin()
	def deleteKey(self, i):
		self.decreaseKey(i, float("-inf"))
		self.extractMin()

	# Get the minimum element from the heap
	def getMin(self):
		return self.heap[0]

#creating Min Heap of size n
heapObj = MinHeap()
n = input ("Enter number of nodes: ")
print(n)
count = 0
while (count < n):
    count = count + 1
    node = random.randrange(0, 500)
    print(node),
    heapObj.insertKey(node)
print("")

#extracting and printing heap
count = 0
while (count < n):
    count = count + 1
    print heapObj.extractMin(),
print("")
