n, m = map(int, input().split())
hear = set()
for _ in range(n):
    hear.add(input())
see = set()
for _ in range(m):
    see.add(input())

hear_see = sorted(hear & see)
print(len(hear_see))
for person in hear_see:
    print(person)