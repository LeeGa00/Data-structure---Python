
stList = []

class Student:
    def __init__(self,number,name,major):
        self.number = number
        self.name = name
        self.major = major
        self.sco = dict()

    def __repr__(self):
        return self.name + "("+self.number+") - "+self.major

def inputSco():
    stnum = input("학번 :")
    for i in stList:
        if i.number == stnum:
            subname = input("과목 :")
            stsco = input("점수 :")
            i.sco[subname] = stsco
            break
        else:
            print("존재하지 않는 학번입니다.")

def show():
    stnum = input("학번 :")
    for i in stList:
        if i.number == stnum:
            print(i.sco)
            break
        else:
            print("존재하지 않는 학번입니다.")

def showAll():
    t = ''
    for i in stList:
        if i.number[:2] != t:
            t = i.number[:2]
            print("===="+t+"====")
        print(i)

while True:
    print("1. 학생 정보 기입\n2. 학생 점수 기입\n3. 학생 점수 조회\n4. 전체 학생 목록\n5. 나가기")
    choice = int(input())
    if choice == 1:
        stnum = input("학번 :")
        stname = input("이름 :")
        stmajor = input("전공 :")
        stList.append(Student(stnum,stname,stmajor))
        for i in range(len(stList)):
            for j in range(len(stList)-1):
                if stList[j].number > stList[j+1].number:
                    stList[j],stList[j+1] = stList[j+1],stList[j]
        print(stname+"님 정보 기입 완료!")
    elif choice == 2:
        inputSco()
    elif choice == 3:
        show()
    elif choice == 4:
        showAll()
    elif choice == 5:
        print("시스템 종료")
        break
    else:
        print("잘못 입력하셨습니다.")
        continue
        

        
        

