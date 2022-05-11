n = int(input())

max_room = 1
layer = 1

while n > max_room:
    max_room += 6 * layer
    layer += 1

print(layer)