

def slove(total_capcity, bucket_list):
    total = sum(bucket_list)
    max_bucket = max(bucket_list)
    if total < total_capcity:
        return []
    tmp = [0] * len(bucket_list)
    sub = [0] * len(bucket_list)
    # i为最大容量
    for i in range(max_bucket, -1, -1):
        for j in range(len(bucket_list)):
            if bucket_list[j] >= i:
                sub[j] = bucket_list[j] - i
                tmp[j] = i
            else:
                sub[j] = 0
                tmp[j] = bucket_list[j]
        if sum(tmp) <= total_capcity:
            return sub
            break




if __name__ == "__main__":
    total_capcity, bucket_num = map(int, input().split())
    bucket_list = list(map(int, input().split()))
    sub = slove(total_capcity, bucket_list)
    print(sub)