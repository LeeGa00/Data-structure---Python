from 연결스택 import *

backStack = Stack()
forwardStack = Stack()

while True:
    if website == 'head':
        website = '빈 페이지'
    print("현재 페이지 : "+ website)
    print("1. 페이지 이동\n2. 뒤로기가\n3. 앞으로 가기\n4. 나가기")
    choice = int(input("선택: "))
    
    if choice == 1:
        website = input("이동할 페이지 : ")
        backStack.push(website)
        back = Stack()
        
    elif choice == 2:
        if backStack.is_empty():
            print("기록이 없읍. 불가능")
        else:
            forwardStack.push(backStack.top.data)
            backStack.pop()
            print()
            website = backStack.top.data
            
    elif choice == 3:
        if forwardStack.is_empty():
            print("기록이 없읍. 불가능")
        else:
            backStack.push(forwardStack.top.data)
            forwardStack.pop()
            print()
            website = backStack.top.data
    else:
        print("GOOD BYE")
        break
