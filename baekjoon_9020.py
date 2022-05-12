def is_prime(num):
    if num == 1:
        return False
    else:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

prime_list = []
for i in range(2, 10000):
    if is_prime(i) == True:
        prime_list.append(i)

t = int(input())
for i in range(t):
    num = int(input())
    for check in range(num//2, 0, -1):
        if (check in prime_list) and (num-check in prime_list):
            print(check, num-check)
            break