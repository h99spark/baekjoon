n, k = map(int, input().split())
temperature = list(map(int, input().split()))

dp = [None] * (n-k+1)
dp[0] = sum(temperature[:k])
for i in range(1, n-k+1):
    dp[i] = dp[i-1] + temperature[i+k-1] - temperature[i-1]

print(max(dp))