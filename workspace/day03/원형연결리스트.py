class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head  = Node('head')
        self.count = 0

    def append(self,data):
        newNode = Node(data)
        curr = self.head
        for i in range(self.count):
            curr = curr.next
        curr.next = newNode
        newNode.next = self.head
        self.count += 1

    def insert(data,idx):
        newNode = Node(data)
        curr = self.head
        for i in range(idx):
            curr = curr.next
        newNode.next = curr.next
        curr.next = newNode
        self.count += 1

    def updata(self,idx, newData):
        curr = self.head
        for i in range(idx+1):
            curr = curr.next
        curr.data = newData

    def delete(self.idx):
        curr= self.head
        for i in range(idx):
            curr = curr.next
        curr.next = curr.next.next
        self.count -= 1

    def get(self):
        curr = self.head
        for i in range(idx+1):
            curr = curr.next
        return curr.data
        
    def show(self):
        curr = self.head
        for i in range(self.count):
            print(curr.data, end = '->')
            curr = curr.next
        print(curr.data)

            
