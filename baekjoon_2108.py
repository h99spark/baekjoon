import sys
from collections import Counter

n= int(sys.stdin.readline().strip())
numbers = [int(sys.stdin.readline().strip()) for _ in range(n)]

# print(f'{sum(numbers) / n:.0f}')
print(round(sum(numbers)/n))

numbers.sort()
print(numbers[n//2])

cnt = Counter(numbers).most_common(2)
if len(cnt) >=2:
    if cnt[0][1] == cnt[1][1]:
        print(cnt[1][0])
    else:
        print(cnt[0][0])
else:
    print(cnt[0][0])

print(numbers[-1] - numbers[0])
