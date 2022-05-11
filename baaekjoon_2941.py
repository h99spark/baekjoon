croatian = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input()
for element in croatian:
    word = word.replace(element, '.')

print(len(word))