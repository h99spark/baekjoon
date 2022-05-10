num_list = set(range(1, 10000))
have_generator = set()

for num in num_list:
    generated_num = num + sum(list(map(int, str(num))))
    have_generator.add(generated_num)

self_list = num_list - have_generator
for num in sorted(self_list):
    print(num)