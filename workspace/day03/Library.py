from 이중연결리스트 import *

bookList = DoubleLinkedList()

class Book:
    def __init__(self,num,name,author):
        self.num = num
        self.name = name
        self.author = author

    #객체 출력시 나올 문자열 설정
    def __repr__(self):
        return self.num+'. '+self.name+"("+self.author+")"
        
    
def register():
    num = int(input("도서번호 :"))
    name = input("도서이름) :")
    author = input("저자 :")
    newBook = Book(num,name,author)
    bookList.append(newBook)
    print(newBook)
    print("등록완료")

def bookDele():
    num = int(input("도서번호 :"))
    flag = False
    for i in range(bookList.count):
        if bookList[i].get(i).num == num:
            bookList.delete(i)
            flag = True
            break
    if not flag:
        print("Wrong Numver")

def bookGet():
    result = set()
    keyword = input('검색할 키워드 :')
    for i in range(bookList.count):
        if keyword in bookList.get(i).author:
            result.add(bookList.get(i))
        if keyword in bookList.get(i).bookname:
            result.add(bookList.get(i))

    for book in result:
        print(book)

def bookShow():
    for i in range(bookList.count):
        print(bookList.get(i))

while(True):
    choice = int(input("1-5 :"))
    if choice == 1:
        register()
    elif choice == 2:
        bookDele()
    elif choice == 3:
        bookGet()
    elif choice == 4:
        bookShow()
    else:
        exit()
        
    
