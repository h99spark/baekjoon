width, height, x0, y0, player_num = map(int, input().split())
players = []
for _ in range(player_num):
    x, y = map(int, input().split())
    players.append([x,y])

cnt = 0
for player in players:
    if (x0 <= player[0] <= x0+width) and (y0 <= player[1] <= y0+height):
        cnt += 1
    elif (x0-player[0])**2 + (y0+height//2-player[1])**2 <= (height//2)**2:
        cnt += 1
    elif (x0+width-player[0])**2 + (y0+height//2-player[1])**2 <= (height//2)**2:
        cnt += 1

print(cnt)