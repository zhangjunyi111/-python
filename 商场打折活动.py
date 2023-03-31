

# 满减接口
def full_subtraction(price, m):
    '''

    :param price: price是满减前的价格
    :param m: m是代表优惠券的数量
    :return: 满减以后优惠券的数量，满减以后的价格
    '''

    n = int(price/100)
    count = min(m, n)
    price -= count * 10
    m -= count
    return price, count


def discount(price,m):
    '''

    :param price: 打折前的价格
    :param m: 打折前的打折券的数量
    :return:
    '''
    if m > 0:
        price *= 0.92
        count = 1
    else:
        count = 0
    return price, count


def free(price, n):
    '''

    :param price: 使用无门槛优惠券前的价格
    :param n: 无门槛券的数量
    :return: 返回使用无门槛券后的价格和无门槛券的数量
    '''
    count = 0
    while price > 0 and n > 0:
        price -= 5
        n -= 1
        count += 1
        price = max(price, 0)
    return price, count


def slove(m, n, k, price):
    result = []
    # 方案1
    # 打折

    discountresult = discount(price, n)

    # 满减结果m
    full_subtractionresult = full_subtraction(discountresult[0], m)

    # 将方案1的结果添加到结果列表中
    result.append([full_subtractionresult[0], discountresult[1] + full_subtractionresult[1]])

    # 方案2
    # 满减 +
    full_subtractionresult = full_subtraction(price, m)
    # 打折
    discountresult = discount(full_subtractionresult[0], n)

    # 将方案2的结果添加到结果列表中

    result.append([discountresult[0], full_subtractionresult[1] +discountresult[1]])

    # 方案3
    # 打折
    discountresult = discount(price, n)

    # 使用无门槛券
    freesult = free(discountresult[0], k)

    # 将方案3的结果添加到结果列表中
    result.append([freesult[0], freesult[1] + discountresult[1]])

    # 方案4
    # 使用满减券
    full_subtractionresult = full_subtraction(price, m)

    # 使用满减券后再使用无门槛券
    freesult = free(full_subtractionresult[0], k)

    # 将方案4的结果添加到结果列表中
    result.append([freesult[0], freesult[1] + full_subtractionresult[1]])

    result.sort(key=lambda x: x[0])
    return result[0]



if __name__ == "__main__":
    '''
    俩俩组合，无门槛的使用券必须放到最后
    1.使用打折券，满减券
    2.使用满减券，打折券
    3.使用打折券，无门槛券
    4.使用满减券，打折券
    '''
    # m,n,k分别为满减，打折，无门槛的券的数量

    m, n, k = map(int, input().split())
    people_number = int(input())
    prices = [int(input()) for i in range(people_number)]
    print(prices)
    for i in range(people_number):
        print(prices[i])
        print(slove(m, n, k, prices[i]))


