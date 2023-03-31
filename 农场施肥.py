import math

def slove(m, n, fileds):

    for i in range(fileds[0], fileds[-1]):
        days = 0
        for j in fileds:
            filed = j
            if j <= i:
                days += 1
            else:
                days += math.ceil(j/i)
                if days > n:
                    break
        if days == n:
            return i
    return -1





if __name__ == "__main__":
    #  接收fillds元素的个数和目标天数
    m, n = map(int, input().split())
    fileds = list(map(int, input().split()))
    if n < m:
        print("-1")
    else:
        print(slove(m, n, fileds))