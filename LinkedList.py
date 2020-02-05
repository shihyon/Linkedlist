import node
class LinkedList():
	def __init__(self):
		self.head = None
		self.count = 0

	def insertHead(self,data):
		self.count += 1
		newNode = node.Node(data)
		
		if self.head is None:
			self.head = newNode
		else:
			newNode.nextNode = self.head
			self.head = newNode

	def linkSize(self):
		return self.count

	def insertTail(self, data):
		self.count += 1
		#newNode = Node(data)
		if self.head is None:
			self.insertHead(data)
			return
		self.count += 1
		newNode = node.Node(data)
		NodePointer = self.head

		while NodePointer.nextNode is not None:
			NodePointer = NodePointer.nextNode
		NodePointer.nextNode = newNode

	def remove(self, data):
		if self.head is not None:
			if data == self.head.data:
				self.head = self.head.nextNode
				self.count -= 1
			else:
				value = self.head.nextNode.remove(data, self.head)
				print("value is ",value)
				if value == True:
					print("return is True?", self.count)
					self.count -=1

	def traverseList(self):
		pointerNode = self.head
		while pointerNode is not None:
			print("%d" % pointerNode.data)
			pointerNode = pointerNode.nextNode


