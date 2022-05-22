import sys
input = sys.stdin.readline

string = input()
questions = int(input())
dp = [[0 for j in range(len(string))] for i in range(26)]
for alpabet in range(97, 123):
    for i in range(len(string)):
        if string[i] == chr(alpabet):
            dp[alpabet-97][i] = dp[alpabet-97][i-1] + 1
        else:
            dp[alpabet-97][i] = dp[alpabet-97][i-1]


for _ in range(questions):
    alpha, start, end = input().split()
    start = int(start)
    end = int(end)
    if start == 0:
        print(dp[ord(alpha)-97][end])
    else:
        print(dp[ord(alpha)-97][end] - dp[ord(alpha)-97][start-1])