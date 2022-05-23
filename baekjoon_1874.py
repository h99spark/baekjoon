n = int(input())
stack = []
ans = []
cnt = 1
possible = True

for _ in range(n):
    target = int(input())

    while cnt <= target:
        stack.append(cnt)
        ans.append('+')
        cnt += 1

    if target == stack.pop():
        ans.append('-')
    else:
        print('NO')
        possible = False
        break

if possible:
    for i in ans:
        print(i)