class ReversedLinkedList:
    def __init__(self, node = None):
        self.Next = node
        node.Previous = self

    def __iter__(self):
        self.a = self.Next
    
    def __next__(self):
        x = self.a
        self.a = self.a.Next
        return x
    
    def Push(self, newNode):
        newNode.Next = self.Next
        if self.Next != None:
            self.Next.Previous = newNode
        self.Next = newNode

    def Append(self, newNode):
        if self.Next == None:
            self.Next = newNode
            newNode.Previous.Next = self
            return
        
        node = self.Next
        previousNode = None
        while node.Next != None:
            previousNode = node
            node = node.Next
        else:
            previousNode = node
        
        node.Next = newNode
        newNode.Previous = previousNode
        
    def Pop(self):
        node = self
        while node.Next != None:
            if node.Next.Next == None:
                node.Next = None
                return
            else:
                node = node.Next
    
    def PreviousAt(self, index):
        node = self
        i = 0
        while node.Next != None:
            print(i)
            if i == index:
                return node.Next.Previous
            else:
                node = node.Next
            i += 1

        return None

    def GetAt(self, index):
        node = self
        i = 0
        while node.Next != None:
            if i == index:
                return node.Next
            else:
                node = node.Next
            i += 1
        else:
            return None

    def Count(self):
        node = self
        i = 0
        while node.Next != None:
            node = node.Next
            i += 1
        
        return i

    def RemoveAt(self, index):
        node = self
        i = 0
        previousNode = None
        nextNode = None
        while node.Next != None:
            if i == index:
                previousNode = node.Next.Previous
                if node.Next.Next != None:
                    nextNode = node.Next.Next
                node.Next = None
            else:
                node = node.Next
            i += 1
        if nextNode != None and previousNode != None:
            previousNode.Next = nextNode

        if previousNode != None and nextNode != None:
            nextNode.Previous = previousNode