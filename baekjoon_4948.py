def is_prime(num):
    if num == 1:
        return False
    else:
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                return False
        return True

prime_list = []
for i in range(1, 123456*2):
    if is_prime(i):
        prime_list.append(i)

while True:
    n = int(input())
    if n == 0:
        break
    else:
        cnt = 0
        for prime in prime_list:
            if n < prime <= 2*n:
                cnt += 1
        print(cnt)
