import sys

def binary_search(array, goal):
    start = 0
    end = len(array) - 1

    while start <= end:
        mid = (start + end) // 2
        if array[mid] == goal:
            return mid
        elif array[mid] > goal:
            end = mid - 1
        else:
            start = mid + 1
    return None

n, m  = map(int, input().split())
words = [sys.stdin.readline().split() for _ in range(n)]
targets = [sys.stdin.readline().split() for _ in range(m)]

words.sort()
cnt = 0
for target in targets:
    if binary_search(words, target) is not None:
        cnt += 1
print(cnt)
