import LinkedList

linkedList = LinkedList.LinkedList()

linkedList.insertHead(12)
linkedList.insertHead(122)
linkedList.insertHead(50)
linkedList.insertHead(1000)
linkedList.traverseList()

print("========> remove node 12")
linkedList.remove(66)
linkedList.traverseList()
print("link size is ",linkedList.linkSize())


