class LinkedList:
    def __init__(self, node = None):
        self.Next = node
        
    def Push(self, newNode):
        if self.Next == None:
            self.Next = newNode
            return
        head = self.Next
        while head.Next != None:
            head = head.Next

        head.Next = newNode
        
    def Pop(self):
        node = self
        while node.Next != None:
            if node.Next.Next == None:
                # del node.Next
                node.Next = None
                return
            else:
                node = node.Next
                
    def RemoveAt(self, index):
        node = self
        i = 0
        previousNode = None
        nextNode = None
        while node.Next != None:
            previousNode = node
            if i == index:
                nextNode = node.Next.Next
                node.Next = None
            else:
                node = node.Next
            i += 1
        if nextNode != None:
            previousNode.Next = nextNode
        else:
            previousNode.Next = None