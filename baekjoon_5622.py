dial = [3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,8,8,8,8,9,9,9,10,10,10,10]
n = input()
sum = 0
for c in n:
    sum += dial[ord(c)-65]
print(sum)