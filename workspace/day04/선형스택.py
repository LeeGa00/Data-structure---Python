MAX_SIZE = 5
class Node(self,data):
    self.data = data

class Stack:
    def __init__(self):
        self.stackList = list()
        self.top = 0

    def pust(self,data):
        if not self.is_full():
            newNode = Node(data)
            self.stackList.insert(self.top,newNode)
            self.top+=1
        else:
            print('stack overflow')

    def pop(self,data):
        if not self.is_empty():
            print(self.stackList[self.top-1].data)
            del self.stackList[self.top-1]
            self.top-=1
        else:
            print('stack empty!')

    #메소드 이름에 is, has가 있다면 보통 리턴은 Bool타입(True,False)
    def is_empty(self):
        return self.top==0

    def is_full(self):
        return self.top == MAX_SIZE

    
