class LinkedList:
    def __init__(self):
        self.Next = None
        
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