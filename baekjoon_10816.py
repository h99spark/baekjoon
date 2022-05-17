n = int(input())
cards = list(map(int, input().split()))
m = int(input())
targets = list(map(int, input().split()))

cnt_dict = dict()
for card in cards:
    if card not in cnt_dict:
        cnt_dict[card] = 1
    else:
        cnt_dict[card] += 1

for target in targets:
    if target in cnt_dict:
        print(cnt_dict[target], end=' ')
    else:
        print(0, end= ' ')