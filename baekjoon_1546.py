n = int(input())
scores = list(map(int, input().split()))
print(sum(scores)*100/(n*max(scores)))