#편돌이

#안녕하세요 세븐일레븐입니다

# 냉동식품
#    1.냉동식품 추가하기
#    2. 폐기물 빼기
#    3. 뒤로가기
# 음료수
#   1. 음료수 추가하기
#   2. 음료수 빼기
#   3. 뒤로가기
# 나가기

from 연결큐 import *

print("안녕하세요 세븐일레븐입니다")

food = LinkedQueue()
drink = LinkedQueue()

while True:
    print("1. 냉동식품\n2. 음료수\n3. 나가기")
    choice = int(input())
    if choice== 1:
        print("1. 냉동식품 추가\n2. 냉동식품 폐기 \n3. 뒤로가기")
        choice = int(input())
        if choice == 1:
            name = input("냉동식품 이름 : ")
            food.enQueue(name)
            print(name+" 추가 완료!\n목록")
            food.show()
        elif choice == 2:
            print(food.deQueue()+"폐기 완료")
        else:
            print("메인으로 이동")
            continue
    elif choice == 2:
        print("1. 음료수 추가\n2. 음료수 폐기 \n3. 뒤로가기")
        choice = int(input())
        if choice == 1:
            name = input("음료수 이름 : ")
            drink.enQueue(name)
            drink.show()
        elif choice == 2:
            print(drink.deQueue()+"폐기 완료")
        else:
            print("메인으로 이동")
            continue
    else:
        print("프로그램 종료")
        break
    
