#연결리스트.py에 있는 모든 내용을 추가하기
from 연결리스트 import *

class User:
    def __init__(self,userid,userpw,username):
        self.userid = userid
        self.userpw = userpw
        self.username = username

userList = LinkedList()

print("==========UMS==========")

while True:
    print("1. 회원가입\n2. 로그인\n3. 나가기")
    choice = int(input())
    if choice == 1:
        #회원가입
        userid = input("아이디 :")
        userpw = input("비밀번호 :")
        username = input("이름 :")
        newUser = User(userid,userpw,username)
        userList.append(newUser)
        print(username+"님 가입을 환영합니다")
    elif choice == 2:
        #로그인
        userid = input("아이디 :")
        userpw = input("비밀번호 :")
        
        for i in range(userList.count):
            if userList.get(i).userid == userid and userList.get(i).userpw == userpw:
                print(userList.get(i).username+"님 어서오세요")
                break
    elif choice == 3:
        #나가기
        print("안녕히가세요.")
    else:
        print("잘못 입력하셨습니다.")
