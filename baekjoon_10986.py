n, m = map(int, input().split())
numbers = list(map(int, input().split()))
remainder = [0 for _ in range(m)]

dp = [numbers[0] for _ in range(n)]
for i in range(1, n):
    dp[i] = dp[i-1] + numbers[i]

for i in range(n):
    remainder[dp[i] % m] += 1

ans = 0
for i in range(m):
    if i == 0:
        ans += remainder[i] * (remainder[i]+1) // 2
    else:
        ans += remainder[i] * (remainder[i]-1) // 2
print(ans)