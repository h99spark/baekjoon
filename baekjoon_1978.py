n = int(input())
prime = n
numbers = list(map(int, input().split()))

for num in numbers:
    if num == 1:
        prime -= 1
    else:
        for i in range(2, num):
            if num % i == 0:
                prime -= 1
                break

print(prime)