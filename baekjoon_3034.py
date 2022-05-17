n, width, height = map(int, input().split())
sticks = [int(input()) for _ in range(n)]

diagonal = (width**2 + height**2)**0.5
for stick in sticks:
    if stick > diagonal:
        print('NE')
    else:
        print('DA')
