def valid_paren(s):
    stack = []
    hash = {'(':')', '[':']'}
    for paren in s:
        if paren in hash:
            stack.append(paren)
        elif paren in hash.values():
            if (not stack) or (paren != hash[stack.pop()]):
                return False

    return (stack == [])

while True:
    string = input()
    if string == '.':
        break
    print('yes' if valid_paren(string) else 'no')