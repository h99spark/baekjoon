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


n = int(input())
cards = list(map(int, input().split()))
m = int(input())
targets = list(map(int, input().split()))

cards.sort()
for target in targets:
    if binary_search(cards, target) is not None:
        print(1, end=' ')
    else:
        print(0, end=' ')