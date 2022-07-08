class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedQueue:
    def __init__(self,task):
        self.front = None
        self.rear = None
        self.task = task

    def is_empty(self):
        return self.front is None

    def enQueue(self,data):
        newNode = Node(data)
        if self.is_empty():
            self.front = newNode
        else:
            self.rear.next = newNode
        self.rear = newNode

    def deQueue(self):
        if not self.is_empty():
            data = self.front.data
            self.front = self.front.next
#            if self.front is None:     --> 연결큐가 비어있다는 뜻
#                self.rear = None
            return data
        else:
            print('queue is empty')

    def show(self):
        curr = self.front
        while curr is not None:
            print(curr.data)
            curr = curr.next

num1 = LinkedQueue("입출금 관련 업무")
num2 = LinkedQueue("예금, 대출 관련 업무")
