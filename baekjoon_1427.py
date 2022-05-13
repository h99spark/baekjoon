num = input()
num_list = [int(n) for n in num]

num_list.sort(reverse=True)
for num in num_list:
    print(num, end= '')