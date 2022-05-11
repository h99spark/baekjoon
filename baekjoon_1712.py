tc, vc, p = map(int, input().split())
if p <= vc:
    print(-1)
else:
    print(int(tc / (p-vc)) + 1)
