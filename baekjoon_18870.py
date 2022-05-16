n = int(input())
points = list(map(int, input().split()))

points_unique = list(sorted(set(points)))
points_dict = {points_unique[i]: i for i in range(len(points_unique))}

for point in points:
    print(points_dict[point], end=' ')