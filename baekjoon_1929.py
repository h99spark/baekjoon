m, n = map(int, input().split())

for num in range(m, n+1):
    is_prime = True

    if num == 1:
        continue

    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            is_prime = False
            break

    if is_prime == True:
        print(num)

