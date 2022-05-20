import math

n = int(input())
numbers = [int(input()) for _ in range(n)]
numbers.sort()

gcd_numbers = []
for i in range(len(numbers)-1):
    gcd_numbers.append(numbers[i+1] - numbers[i])

gcd = gcd_numbers[0]
for gcds in gcd_numbers[1:]:
    gcd = math.gcd(gcd, gcds)

result = set()
for i in range(2, int(gcd**0.5)+1):
    if gcd % i == 0:
        result.add(i)
        result.add(gcd // i)
result.add(gcd)

for factor in sorted(list(result)):
    print(factor, end=' ')