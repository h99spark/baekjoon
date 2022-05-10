num_list = [int(input()) for _ in range(3)]
n = str(num_list[0] * num_list[1] * num_list[2])

for i in range(10):
    print(n.count(str(i)))