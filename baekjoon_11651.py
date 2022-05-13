n = int(input())
points = list()

for i in range(n):
    x, y = map(int, input().split())
    points.append([x,y])

points_sorted = sorted(points, key = lambda point : (point[1], point[0]))

for point in points_sorted:
    print(point[0], point[1])