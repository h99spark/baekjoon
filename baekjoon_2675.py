n = int(input())
for _ in range(n):
    n, s = input().split()
    for c in s:
        print(c*int(n), end='')
    print()