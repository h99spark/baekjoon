n = int(input())
numbers = [int(input()) for _ in range(n)]

cnt_list = [0] * (n+1)
for num in numbers:
    cnt_list[num] += 1

for i in range(1, n+1):
    if cnt_list[i] != 0:
        for j in range(cnt_list[i]):
            print(i)
