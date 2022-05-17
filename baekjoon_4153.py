while True:
    triangle = list(map(int, input().split()))
    if triangle[0] == triangle[1] == triangle[2] == 0:
        break
    else:
        triangle.sort()
        if triangle[0]**2 + triangle[1]**2 == triangle[2]**2:
            print('right')
        else:
            print('wrong')
