import sys

n, m = map(int, sys.stdin.readline().strip().split())
dogam_name = dict()
dogam_number = dict()
for i in range(1, n+1):
    name = sys.stdin.readline().strip()
    dogam_name[name] = i
    dogam_number[i] = name

for _ in range(m):
    inp = sys.stdin.readline().strip()
    if inp.isdigit():
        print(dogam_number[int(inp)])
    else:
        print(dogam_name[inp])