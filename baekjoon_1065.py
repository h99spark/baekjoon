n = int(input())

if n < 100:
    print(n)
else:
    hansoo = 0
    for i in range(100, n+1):
        str_i = list(map(int, str(i)))
        if str_i[0] + str_i[2] == 2 * str_i[1]:
            hansoo += 1
    print(hansoo + 99)