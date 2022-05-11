t = int(input())
for _ in range(t):
    h, w, n = map(int, input().split())

    if n % h == 0:
        floor = h
        ho = n // h
    else:
        floor = n % h
        ho = n // h + 1

    print(floor * 100 + ho)