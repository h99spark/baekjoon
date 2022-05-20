from collections import Counter

t = int(input())
for _ in range(t):
    cloth_num = int(input())
    category_list = []
    for _ in range(cloth_num):
        _, category = input().split()
        category_list.append(category)
    category_count = Counter(category_list).most_common()

    ans = 1
    for category in category_count:
        ans *= (category[1] + 1)
    print(ans - 1)