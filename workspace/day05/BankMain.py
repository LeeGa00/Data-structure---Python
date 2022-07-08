#BankMain.py
#1. 대기번호 발급
    #입출금 관련 업무
    #예금, 대출 관련 업무
#2. 순서 확인
    #대기번호 :
#3. 다음 번호 부르기
    #입출금 관련 업무
    #예금, 대출 관련 업무
#4. 나가기

from BankManager import *

print("안녕하세요 국민은행입니다")

while True:
    print("1. 대기번호 발급\n2. 순서확인\n3. 다음 번호 부르기\n4. 나가기")
    choice = int(input())
    if choice == 1:
        print("대기번호 :"+bank.order())
        print("1. 입출금 관련 업무\n2. 예금, 대출 관련 업무")
        choice = int(input())
        numIssue(choice)
    elif choice == 2:
        personNum = int(input("당신의 대기번호:"))
        orderCheck(personNum)
    elif choice == 3:
        print("1. 입출금 관련 업무\n2. 예금, 대출 관련 업무")
        choice = int(input())
        callNum(choice)
    else:
        print("프로그램 종료")
        break
    
