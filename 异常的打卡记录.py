import sys
n = int(input())
# 将所有员工的打卡记录以列表的形式存放到打开记录集合
# 中clock_records，按次数循环接受数据并用split处理
clock_records = [input().split(",") for i in range(n)]
# print(check_records)

# 定义自己的函数减少耦合
def getresult(clock_records):
    # 定义员工字典，存放员工id的所有打卡记录
    employees = {}
    # 定义集合ans存放异常的打开记录的索引，用索引存放不合理的打开数据在最后根据索引输出
    ans = set()
    for i in range(len(clock_records)):
        # 列表的整体赋值给多个变量
        id, time, distance, ActuralDeviceNumber, \
        ResigterDeviceNumber = clock_records[i]

        if ActuralDeviceNumber != ResigterDeviceNumber:
            ans.add(clock_records[i])
        # 追加索引,将第一步排除后的结果存入到字典中
        clock_record = [id, time, distance, ActuralDeviceNumber,
        ResigterDeviceNumber, i]

        # 字典的get方法要学会使用
        if employees.get(id) is None:
            employees[id] = [clock_record]
        else:
            employees[id].append(clock_record)
    print(employees)
    print(ans)
    # 对比同一个员工的多条打卡记录，如果存在打卡距离大于5km.，打卡时间间隔小于60的记录，将索引加入ans
    # 同一员工的打卡数据用列表进行存储，用id标识员工，并进行员工数据的遍历
    for id in employees.keys():
        records = employees[id]
        n = len(records)
        records.sort(key=lambda x: x[1])
        # 比较员工的每条数据的time和distance使用2个for循环遍历
        for i in range(n):
            time1 = int(records[i][1])
            distance1 = int(records[i][2])
            for j in range(i+1, n):
                # 字符串在进行比较事，需要转化为整形进行比较输出
                time2 = int(records[j][1])
                distance2 = int(records[j][2])
                if time2 - time1 >= 60:
                    break
                else:
                    # 距离使用绝对值函数计算
                    if abs(distance2-distance1) > 5:
                        if records[i][5] not in ans:
                            ans.add(records[i][5])
                        if records[j][5] not in ans:
                            ans.add(records[j][5])

    if len(ans) > 0:
        ans = list(ans)
        # 使用排序函数，保证按输入顺序输出
        ans.sort()
        newrecords = []
        # 输出处理输出用join对列表进行拼接输出
        for i in ans:
            record = ",".join(clock_records[i])
            newrecords.append(record)
        print(";".join(newrecords))
    else:
        return []



getresult(clock_records)











