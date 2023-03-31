import sys
input_str = input().split()
boxs = list(input_str[0])
number = int(input_str[1])
s = len(boxs) % number
L = []

# 预计可以排x行

x = len(boxs)//number
left = boxs[-(len(boxs) % number):]
for k in range(number-len(left)):
    left.append("0")

for i in range(x):
    if i % 2 == 0:
        res = boxs[i*number:(i+1)*number]
        L.append(res)
        # boxs = boxs[(i+1)*number : ]
    else:
        res = boxs[i*number:(i+1)*number]
        res = res[::-1]
        L.append(res)
        # boxs = boxs[(i+1)*number:]

L.append(left)
print(L)
L = list(map(list, zip(*L)))
print(L)

for x in L:
    # print()
    res = ""
    for j in x:
        if j != "0":
            res += j
    print(res)

