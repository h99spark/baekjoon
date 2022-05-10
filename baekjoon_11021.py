n = int(input())

for i in range(1, n+1):
    a, b = map(int, input().split())
    print(f'Case #{i}: {a+b}')
    # print('Case #%d: %d' % (i, a+b))