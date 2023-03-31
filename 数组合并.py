import sys
k = input()
n = int(input())


builder = ""
index = 0

numArrays = [input().split(",") for i in range(n)]
while len(numArrays) > 0:
    singleArray = numArrays[index]
    for i in range(int(k)):
        if len(singleArray) == 0:
            numArrays.pop(index)
            index -= 1
            break
        builder += str(singleArray[0])+","
        singleArray.pop(0)
    index += 1
    if index >= len(numArrays):
        index = 0



