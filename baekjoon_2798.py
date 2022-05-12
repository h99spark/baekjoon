n, goal = map(int, input().split())
cards = list(map(int, input().split()))

sum = 0
for i in range(0, n-2):
    for j in  range(i+1, n-1):
        for k in range(j+1, n):
            if cards[i] + cards[j] + cards[k] <= goal:
                sum = max(sum, cards[i] + cards[j] + cards[k])

print(sum)