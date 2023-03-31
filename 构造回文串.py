s = input()

# 算法入口
def getresult(s):
    print("start")
    count = {}
    for x in s:
        if x not in count:
            count[x] = 1
        else:
            count[x] += 1
    ans = []
    mid = ""
    for c in count:
        if count[c] >= 2:
            n = count[c] // 2
            ans += [c]*n
        if count[c] % 2 != 0 and (mid == "" or c< mid):
            mid = c
    ans.sort()
    left = "".join(ans)
    ans.reverse()
    right = "".join(ans)
    return left+mid+right

print(getresult(s))




