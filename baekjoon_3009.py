x_point = []
y_point = []
for i in range(3):
    x, y = input().split()
    x_point.append(x)
    y_point.append(y)

if x_point[0] == x_point[1]:
    print(x_point[2], end= ' ')
elif x_point[0] == x_point[2]:
    print(x_point[1], end=' ')
else:
    print(x_point[0], end=' ')

if y_point[0] == y_point[1]:
    print(y_point[2], end=' ')
elif y_point[0] == y_point[2]:
    print(y_point[1], end=' ')
else:
    print(y_point[0], end=' ')