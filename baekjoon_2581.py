m = int(input())
n = int(input())

prime_list = [i for i in range(m, n+1)]
for num in range(m, n+1):
    if num == 1:
        prime_list.remove(num)
    else:
        for i in range(2, num):
            if num % i == 0:
                prime_list.remove(num)
                break

if not prime_list:
    print(-1)
else:
    print(sum(prime_list))
    print(min(prime_list))