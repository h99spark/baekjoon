n = int(input())
numbers = [int(input()) for i in range(n)]

for i in range(n):
    for j in range(0, n-i-1):
        if numbers[j] > numbers[j+1]:
            numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

for num in numbers:
    print(num)