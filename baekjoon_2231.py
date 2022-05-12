n = int(input())
generator = 0

for i in range(n):
    generated = i
    for c in str(i):
        generated += int(c)
    if generated == n:
        generator = i
        break

print(generator)

