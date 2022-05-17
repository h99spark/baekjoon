t = int(input())
for _ in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    distance = ((x2-x1)**2 + (y2-y1)**2)**0.5

    if distance == 0 and r2 == r1:
        print(-1)
    elif abs(r2 - r1) < distance < r2 + r1:
        print(2)
    elif distance == abs(r2-r1) or distance == r2 + r1:
        print(1)
    else:
        print(0)