dataList = [10,8,1,4,9,3,5,6,2,7]
size = 10

for i in range(size-1):
    min = i
    for j in range(i+1,size):
        if dataList[min] >= dataList[j]:
            min = j
    dataList[i], dataList[min] = dataList[min], dataList[i]

print(dataList)

