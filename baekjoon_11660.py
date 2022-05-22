import sys
input = sys.stdin.readline

n, m = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(n)]
dp = [[0]*(n+1) for _ in range(n+1)]

for row in range(1, n+1):
    for column in range(1, n+1):
        dp[row][column] = dp[row][column-1] + dp[row-1][column] - dp[row-1][column-1] + array[row-1][column-1]

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    print(dp[x2][y2] - dp[x1-1][y2] - dp[x2][y1-1] + dp[x1-1][y1-1])
