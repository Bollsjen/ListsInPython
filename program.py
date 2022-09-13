from LinkedList import LinkedList

class Node:
    def __init__(self, data, next):
        self.Data = data
        self.Next = next
        
    def __str__(self):
        return self.Data

class Fisk:
    def __init__(self, data, next):
        self.Data = data
        self.Next = next

class Program:
    def Run(self):
        head = LinkedList(Node("Fisk", None))
        head.Push(Node("Torsk", None))
        head.Push(Node("Rødspætte", None))
        head.Push(Fisk("Dette er faktisk en fisk", None))
        self.PrintList(head)
        head.Pop()
        head.Pop()
        head.Pop()
        self.PrintList(head)
        
        
        head.Push(Node("Spade", None))
        self.PrintList(head)
        self.PrintToList(head)
        
        head.RemoveAt(1)
        self.PrintList(head)
        
        
        head.RemoveAt(0)
        self.PrintList(head)

    def PrintList(self,head):
        result = ""
        while head.Next != None:
            result = result + head.Next.Data + ", "
            head = head.Next

        print(result)
        
    def PrintToList(self, head):
        stringDims = "["
        for item in head.ToList():
            stringDims = stringDims + item.Data + ", "
        stringDims += "]"
        print(stringDims)


program = Program()
program.Run()