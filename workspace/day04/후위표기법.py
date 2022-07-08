#'문자열'.isdigit()
#'문자열'[0]

from 연결스택 import *

def getPriority(oper):
    if oper == '+' or oper == '-':
        return 1
    elif oper == '/' or oper == '*':
        return 2
    else:
        return 0

liStack = Stack()
#괄호 없는 수식
'''
while True:
    eq = input('수식입력: ')
    for i in range(len(eq)):
        if eq[i].isdigit():
            print(eq[i],end='')
        else:
            if liStack.is_empty():
                liStack.push(eq[i])
            else:
                while(getPriority(liStack.top.data) >= getPriority(eq[i])):
                    liStack.pop()
                    if liStack.is_empty():
                        break
                liStack.push(eq[i])
    while not liStack.is_empty():
        liStack.pop()
'''

#괄호 있는 수식
while True:
    eq = input('수식입력: ')
    for i in range(len(eq)):
        if eq[i].isdigit():
            print(eq[i],end='')
        else:
            if liStack.is_empty() or eq[i] == '(':
                liStack.push(eq[i])
            else:
                if eq[i]==')':
                    while not liStack.top.data == '(':
                        operList.pop()
                else:
                    while(getPriority(liStack.top.data) >= getPriority(eq[i])):
                        liStack.pop()
                        if liStack.is_empty():
                            break
                    liStack.push(eq[i])
    while not liStack.is_empty():
        if liStack.top.data == '(':
            break
        liStack.pop()
    print()        
