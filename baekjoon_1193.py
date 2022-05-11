n = int(input())

line = 1
max_num = 1
while n > max_num:
    line += 1
    max_num += line

gap = max_num - n
if line % 2 == 0:
    print(f'{line-gap}/{gap+1}')
else:
    print(f'{gap+1}/{line-gap}')