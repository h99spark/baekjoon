fruit = int(input())
list = []
for _ in range(6):
    direction, length = map(int, input().split())
    list.append([direction, length])

big_rectangle = 0
index = None
for i in range(6):
    tmp = list[i][1] * list[(i+1) % 6][1]
    if big_rectangle < tmp:
        big_rectangle = tmp
        index = i
small_rectangle = list[(index+3)%6][1] * list[(index+4)%6][1]

print(fruit * (big_rectangle - small_rectangle))