import sys
# n代表酒店的数量，k代表需要挑选的酒店的数量，x代表心里价位
# 如果下面n，k,x都需要的是整数，那么直接用map映射为整数后再处理
n, k, x = map(int, input().split())
prices = list(map(int, input().split()))
prices.sort()
# 求酒店的价格和预期x之间的差距列表price_rate
price_rate = [(price, abs(price - int(x))) for price in prices]
price_rate.sort(key=lambda x: x[1])
print(price_rate)
piecked_price = [price_rate[i][0] for i in range(int(k))]
print(*piecked_price)
