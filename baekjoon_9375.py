t = int(input())
for _ in range(t):
    cloth_num = int(input())
    cloth_dict = {}
    for _ in range(cloth_num):
        cloth, category = input().split()
        if category in cloth_dict:
            cloth_dict[category] += 1
        else:
            cloth_dict[category] = 1

    ans = 1
    for key in cloth_dict:
        ans *= (cloth_dict[key]+1)
    print(ans-1)