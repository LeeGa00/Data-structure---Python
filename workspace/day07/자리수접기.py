MAX = 7
dataList = ['' for i in range(MAX)]

def h(x):
    return x%MAX

def digitFolding(s):
    tot = 0
    for ch in s:
        #ord('문자') : 아스키코드로 변환
        #int('1') : 1
        #ord('1') : 49
        tot += ord(ch)
    return tot

while True:
    s = input('지정할 문자열 : ')
    saveIdx = h(digitFolding(s))
    dataList[saveIdx] = s
    print("=========================")
    for i in range(MAX):
        print(i,':',dataList[i])
        
        
