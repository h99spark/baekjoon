city_num = int(input())
road = list(map(int, input().split()))
price = list(map(int, input().split()))

sum = 0
oil_price = price[0]
for i in range(0, city_num-1):
    oil_price = min(price[i], oil_price)
    sum += oil_price * road[i]

print(sum)