
# 接收工作时长，工作数量
worktime, worknum = map(int, input().split())
works = []

# 接收works
for i in range(worknum):
    time, value = map(int, input().split())
    works.append([time, value])

dp = [[ 0 for i in range(worktime+1)] for j in range(worknum)]
for j in range(worktime):
    if  works[0][0] <= worktime:
        dp[0][j] = works[0][1]

for i in range(1, worknum):
    for j in range(1, worktime+1):
        if works[i][0] <= j:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-works[i][0]]+works[i][1])
        else:
            dp[i][j] = dp[i-1][j]

for x in range(len(dp)):
    print(dp[worknum-1][worktime])

