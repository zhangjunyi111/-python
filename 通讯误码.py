def slove(codes):
    code_count = {}
    max_code = set()
    max_count = 0
    for code in codes:
        if code not in code_count:
            code_count[code] = 1
        else:
            code_count[code] += 1

    for code, count in code_count.items():
        max_count = max(max_count, count)

    for code, count in code_count.items():
        if count == max_count:
            max_code.add(code)


    i = 0
    j = len(codes)-1
    minlength = 0
    for code in list(max_code):
        while codes[i] != code:
            i += 1

        while codes[j] != code:
            j -= 1

        if i <= j:
            length = j-i+1
        minlength = min(length, minlength)
    return minlength


if __name__ == "__main__":
    n = int(input())
    code = list(map(int, input().split()))
    print(slove(code))