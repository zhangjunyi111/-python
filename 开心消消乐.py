import sys
# 接收矩阵的行数和列数
rows, cols = map(int,input().split())

# 将没一行添加到矩阵中
matrix = [input().split() for x in range(rows)]


# 定义广度优先搜索的函数
def dfs(x, y):
    '''
    :param x: x是广度优先遍历的起点的横坐标
    :param y: y是广度优先遍历起点的纵坐标
    :return:
    '''
    queue = []
    queue.append([x, y])
    matrix[x][y] = 0
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, 1), (1, 1), (1, -1), (-1, -1)]
    while queue:
        i, j = queue.pop(0)
        for x in range(8):
            newi, newj = i+directions[x][0], j+directions[x][1]
            if 0 <= newi < rows and 0 <= newj < cols:
                if matrix[newi][newj] == "1":
                    queue.append([newi, newj])
                    matrix[newi][newj] = "0"


result = 0
for i in range(rows):
    for j in range(cols):
        if matrix[i][j] == "1":
            dfs(i, j)
            result += 1
print(result)







