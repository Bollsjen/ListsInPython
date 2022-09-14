from LinkedList import LinkedList
from ReversedLinkedList import ReversedLinkedList

class Node:
    def __init__(self, data):
        self.Data = data
        self.Next = None
        
    def __str__(self):
        return self.Data

class Fisk:
    def __init__(self, data):
        self.Data = data
        self.Next = None

class ReverseNode:
    def __init__(self, data):
        self.Data = data
        self.Next = None
        self.Previous = None

class Program:
    def Run(self):
        # head = LinkedList(Node("Fisk"))
        # head.Push(Node("Torsk"))
        # head.Push(Node("Rødspætte"))
        # head.Push(Fisk("Dette er faktisk en fisk"))
        # self.PrintList(head)
        # head.Pop()
        # head.Pop()
        # head.Pop()
        # self.PrintList(head)
        
        
        # head.Push(Node("Spade"))
        # self.PrintList(head)
        # self.PrintToList(head)
        
        # head.RemoveAt(1)
        # self.PrintList(head)
        
        
        # head.RemoveAt(0)
        # self.PrintList(head)

        reverse = ReversedLinkedList(ReverseNode("Spætte"))
        reverse.Push(ReverseNode("Gråspurv"))
        print(reverse.PreviousAt(1).Data)
        print(reverse.GetAt(1).Data)
        reverse.RemoveAt(1)
        print(reverse.GetAt(0).Data)

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