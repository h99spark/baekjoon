def cnt_number(n, k):
    cnt = 0
    while n >= k:
        cnt += n//k
        n //= k
    return cnt

n, m = map(int, input().split())
number_five = cnt_number(n, 5) - cnt_number(m, 5) - cnt_number(n-m, 5)
number_two =  cnt_number(n, 2) - cnt_number(m,  2) - cnt_number(n-m, 2)
print(min(number_two, number_five))