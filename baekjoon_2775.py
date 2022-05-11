t = int(input())
for _ in range(t):
    k = int(input())
    n = int(input())
    residence = [i for i in range(1, n+1)]
    for floor in range(k):
        for room in range(1,n):
            residence[room] += residence[room-1]
    print(residence[-1])