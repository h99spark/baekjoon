import sys

n = int(input())
numbers = [int(sys.stdin.readline()) for i in range(n)]

numbers.sort()

for num in numbers:
    print(num)