rows, cols = map(int, input().split())
# matrix = []
matrix = [input().split() for i in range(rows)]


def caculatearea(i, k) -> int:
    flag = True
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    count = 1
    queue = [[i, k]]
    while queue:
        elemete = queue.pop(0)
        i, k = elemete[0], elemete[1]
        for x in range(4):
            newi, newj = directions[x][0] + i, directions[x][1] + k
            if 0 <= newi < rows and 0 <= newj < cols:
                if matrix[newi][newj] == "o":
                    # 一定要先改值，再退出，如果遇上边界条件
                    matrix[newi][newj] = "x"
                    if newi == 0 or newi == rows-1 or newj == 0 or newj == cols-1:
                        flag = False
                    queue.append([newi, newj])
                    count += 1
    if flag:
        return count
    else:
        return 0


maxArea = 0
zones = {}
for i in range(rows):
    for j in range(cols):
        if i == 0 or i == rows-1 or j == 0 or j == cols-1:
            if matrix[i][j] == "o":
                matrix[i][j] = "x"
                Area = caculatearea(i, j)
                maxArea = max(Area, maxArea)
                if Area > 0:
                    key = str(i)+" "+str(j)
                    zones[key] = Area


maxAreaEntrance = ""
for key, value in zones.items():
    if value == maxArea:
        if maxAreaEntrance == "":
            maxAreaEntrance = key
        else:
            maxAreaEntrance = "more"
            break
if maxArea == 0:
    print("null")
elif maxAreaEntrance == "more":
    print(maxArea)

else:
    print(maxAreaEntrance+" "+str(maxArea))
