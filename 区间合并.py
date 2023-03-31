# 处理输入，接收区间组和连接器
range_str = input()
connect_str = input()

# 解析区间字符串
range_str = range_str.replace("[", "").replace("]", "")

# 解析连接器字符串
connect_str = connect_str.replace("[", "").replace("]", "")

# 打印观察
# print(range_str)
# print(connect_str)

# 定义将字符串转为整型数组的函数split


def split(input_str):
    # 重新定义一份数组，避免在原始字符串上操作
    l1 = []
    while input_str.find(",") != -1:
        found = input_str.find(",")
        number = input_str[0:found]
        l1.append(number)
        input_str = input_str[found+1:]

    # 处理最后一个逗号后面的字符串
    l1.append(int(input_str))
    return l1

# 根据range_str构造区间
# 先转化为整型列表，然后从整型列表中每隔2个数取一次


tmp_ranges = split(range_str)
connectors = split(connect_str)
ranges = []
for i in range(0, len(tmp_ranges), 2):
    ranges.append([tmp_ranges[i], tmp_ranges[i+1]])


def compare(a, b):
    if a[0] > b[0]:
        return False

    if a[0] == b[0]:
        if a[1] > b[1]:
            return False

    return True


def range_sort(ranges):
    for i in range(len(ranges)):
        for j in range(i+1, len(ranges)):
            if not compare(ranges[i], ranges[j]):
                ranges[i], ranges[j] = ranges[j], ranges[i]
    return ranges


ranges = range_sort(ranges)


def megre_ranges(ranges):
    megre_range = [ranges[0]]
    range_diffs = []
    for i in range(1, len(ranges)):
        range1 = megre_range[-1]
        range2 = ranges[i]
        if range1[1] >= range2[0]:
            megre_range.pop()
            megre_range.append([range1[0], max(range1[1], range2[1])])
        else:
            range_diffs.append(range2[0]-range1[1])
            megre_range.append(range2)
    return megre_range, range_diffs


megre_range, range_diff = megre_ranges(ranges)


def connect_ranges(range_diffs, connectors):
    count = 1
    # 计数器初始值表示至少需要一个连接器
    i, j = len(range_diffs)-1 , len(connectors)-1
    while i >= 0 and j >= 0:
        if connectors[j] >= range_diffs[i]:
            j -= 1
        else:
            count += 1
        i -= 1
    return count


print(connect_ranges(range_diff, connectors))





