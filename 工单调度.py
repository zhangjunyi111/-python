import queue

# 获取任务数
num_tasks = int(input())

# 获取每个任务的截止时间和积分

tasks = [list(map(input().split())) for i in range(num_tasks)]


def get_total_score(tasks):
    tasks.sort(key=lambda x: x[0])
    priority_queue = queue.PriorityQueue()

    # 记录总积分和当前时间
    total_score = 0
    cur_time = 0
    for task in tasks:
        end_time, score = task[0], task[1]
        if end_time > cur_time + 1:
            priority_queue.put(score)
            total_score += score
            cur_time += 1
        else:
            if priority_queue.qsize() == 0:
                continue

            min_score = priority_queue.queue[0]
            if score > min_score:
                priority_queue.get()
                priority_queue.put(score)
                total_score += score - min_score
    return total_score









