n = int(input())
meetings = []
for _ in range(n):
    start, end = map(int, input().split())
    meetings.append((start, end))

meetings.sort(key = lambda x: (x[1], x[0]))

end_last = 0
cnt = 0
for meeting in meetings:
    if meeting[0] >= end_last:
        cnt += 1
        end_last = meeting[1]

print(cnt)