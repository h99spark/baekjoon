n = int(input())
for _ in range(n):
    result = list(map(int, input().split()))
    stu_num = result[0]
    avg = sum(result[1:]) / stu_num

    cnt = 0
    for score in result[1:]:
        if score > avg:
            cnt += 1

    print(f'{cnt*100/stu_num:.3f}%')