from random import *

myList = []
i = 10000
while i > 0:
    x = randint(1,10000000)
    if x in myList:
        continue
    if i == 300:
        myNumber = x
    i -= 1
    myList.append(x)

myList.sort()

print(myNumber)
ePivot = i
sPivot = 0

def biSe(myNumber, sPivot, ePivot):
    mid = (sPivot + ePivot) // 2
    # print(mid)
    if myNumber > myList[mid]:
        # print(myNumber, mid+1, ePivot)
        return biSe(myNumber, mid+1, ePivot)
    elif myNumber < myList[mid]:
        # print(myNumber, sPivot, mid-1)
        return biSe(myNumber, sPivot, mid-1)
    else:
        return mid

result = biSe(myNumber,0, 10000)
print(f"내가 찾을 숫자는 ? {myNumber} 전체 리스트 중에 {result+1}번에 있습니다.")