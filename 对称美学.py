

def find(n, k):
    if n == 1:
        return "red"
    length = 2**(n-1)
    if k >= length/2:
        pos = k-length // 2
        return find(n-1, pos)
    else:
        return "blue" if find(n-1, k) == "red" else "red"


if __name__ == "__main__":
    t = int(input())
    cases = [list(map(int, input().split())) for _ in range(t)]
    for case in cases:
        n = case[0]
        k = case[1]
        print(find(n, k))


