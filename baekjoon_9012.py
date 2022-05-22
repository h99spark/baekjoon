def valid_paren(s):
    stack = []
    for p in s:
        if p == '(':
            stack.append(p)
        else:
            if not stack:
                return False
            else:
                stack.pop()
    return True if not stack else False

n = int(input())

for _ in range(n):
    string = input()
    print('YES' if valid_paren(string) else 'NO')

