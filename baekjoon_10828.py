import sys
input = sys.stdin.readline
n = int(input())
stack = []

for _ in range(n):
    s = input().split()
    if s[0] == 'push':
        stack.append(int(s[1]))
    elif s[0] == 'pop':
        print(-1 if stack == [] else stack.pop())
    elif s[0] == 'size':
        print(len(stack))
    elif s[0] == 'empty':
        print(1 if stack == [] else 0)
    elif s[0] == 'top':
        print(-1 if stack == [] else stack[-1])

