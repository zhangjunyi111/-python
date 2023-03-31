
input_str = input()

# 创建一个字符统计器
char_count = {}
for char in input_str:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

char_count["W"] = char_count.get("W", 0)
char_count["S"] = char_count.get("S", 0)
char_count["A"] = char_count.get("A", 0)
char_count["D"] = char_count.get("D", 0)

# 如果四个字符出现的
