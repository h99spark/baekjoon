testcase = int(input())

for _ in range(testcase):
    x1, y1, x2, y2 = map(int, input().split())

    planet_num = int(input())
    cross = 0
    for _ in range(planet_num):
        x, y, r = map(int, input().split())
        distance1 = ((x-x1)**2 + (y-y1)**2)**0.5
        distance2 = ((x-x2)**2 + (y-y2)**2)**0.5
        if (distance1 < r and distance2 > r) or (distance1 > r and distance2 < r):
            cross += 1

    print(cross)