import sys
n, m = map(int, input().split())
numbers = list(map(int, sys.stdin.readline().strip().split()))

dp = [numbers[0]] * n
for i in range(1, n):
    dp[i] = dp[i-1] + numbers[i]

for _ in range(m):
    start, end = map(int, sys.stdin.readline().split())
    if start == 1:
        print(dp[end-1])
    else:
        print(dp[end-1] - dp[start-2])