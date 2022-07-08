from 이중연결리스트 import *

class Book:
    def __init__(self,booknum,bookname,author):
        self.booknum=booknum
        self.bookname=bookname
        self.author=author

    #객체 출력시 나올 문자열 설정
    def __repr__(self):
        return self.booknum+'. '+self.bookname+"("+self.author+")"

bookList = DoubleLinkedList()

def addBook(booknum,bookname,author):
    newBook = Book(booknum,bookname,author)
    bookList.append(newBook)
    return newBook

def deleteBook(deleteNum):
    for i in range(bookList.count):
        if bookList.get(i).booknum == deleteNum:
            bookList.delete(i)
            return True
    return False

def searchBook(keyword):
    result = set()
    keyword = input('검색할 키워드 : ')
    for i in range(bookList.count):
        if keyword in bookList.get(i).author:
            result.add(bookList.get(i))
        if keyword in bookList.get(i).bookname:
            result.add(bookList.get(i))
        return result

def showList():
    result = ""
    for i in range(bookList.count):
        result += repr(bookList.get(i))+"\n"
    return result

        
