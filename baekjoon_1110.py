n = int(input())
temp = n
cycle = 0
while True:
    cycle += 1
    temp = ((temp // 10) + (temp % 10)) % 10 + (temp % 10) * 10
    if temp == n:
        print(cycle)
        break
