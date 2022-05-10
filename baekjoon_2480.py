dice = list(map(int, input().split()))

if dice[0] == dice[1] == dice[2]:
    print(1000 * dice[0] + 10000)
elif (dice[0] == dice[1]) or (dice[1] == dice[2]):
    print(100 * dice[1] + 1000)
elif dice[2] == dice[0]:
    print(100 * dice[0] + 1000)
else:
    print(100 * max(dice))