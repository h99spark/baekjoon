h, m = map(int, input().split())
time = int(input())

present_time = h * 60 + m
finish_time = present_time + time
m = finish_time % 60
h = finish_time // 60
if h >= 24:
    h -= 24

print(h, m)