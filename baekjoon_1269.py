n1, n2 = map(int, input().split())
s1 = set(map(int, input().split()))
s2 = set(map(int, input().split()))
print(len(s1^s2))
