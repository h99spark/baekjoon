def gcd(a,b):
    while b>0:
        a, b = b, a%b
    return a

n = int(input())
ratchets = list(map(int, input().split()))
for ratchet in ratchets[1:]:
    divisor = gcd(ratchets[0], ratchet)
    print(f'{ratchets[0]//divisor}/{ratchet//divisor}')