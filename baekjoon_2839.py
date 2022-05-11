weight = int(input())
if weight == 4 or weight == 7:
    print(-1)
else:
    for five_bag in range(weight//5, -1, -1):
        if (weight - five_bag * 5) % 3 == 0:
            print(int(five_bag + (weight - five_bag * 5) / 3))
            break