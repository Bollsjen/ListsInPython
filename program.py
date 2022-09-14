from LinkedList import LinkedList
from ReversedLinkedList import ReversedLinkedList
from Dictionary import Dictionary

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
        head = LinkedList(Node("Fisk"))
        head.Push(Node("Torsk"))
        head.Push(Node("Rødspætte"))
        head.Push(Fisk("Dette er faktisk en fisk"))
        self.PrintList(head)
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
        
        print(head.GetAt(0).Data)

        # reverse = ReversedLinkedList(ReverseNode("Spætte"))
        # reverse.Append(ReverseNode("Gråspurv"))
        # # reverse.RemoveAt(1)
        # self.PrintList(reverse)
        # reverse.Pop()
        # self.PrintList(reverse)
        
        numbers = Dictionary({"one": 1, "two": 2})
        numbers["three"] = 3
        numbers.update({"four": 4})
        numbers.setdefault("five", 5)
        
        print(numbers)
        print(numbers.Count())
        print(numbers.IsEmpty())
        
        numbers.Remove("three")
        print(numbers)
        print(numbers.Count())
        print(numbers.IsEmpty())
        

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