

def slove(woods, m):
    woods.sort()
    for i in range(m):
        woods[0] += 1
        woods.sort()
    return woods[0]


if __name__ == "__main__":
    n, m = map(int, input().split())
    woods = list(map(int, input().split()))
    print(slove(woods, m))