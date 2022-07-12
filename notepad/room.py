stNum, rMax = map(int,input().split(" "))

stList = [[0 for col in range(2)] for row in range(7)]

for i in range(stNum):
    gender, grade = map(int, input().split(" "))
    stList[grade][gender] += 1

print(stList)

rCnt = 0

for 학년 in range(1,7):
    for 성별 in range(2):
        if stList[학년][성별] != 0:
            rCnt = rCnt + int(stList[학년][성별]/rMax + stList[학년][성별]%rMax)

print(rCnt)