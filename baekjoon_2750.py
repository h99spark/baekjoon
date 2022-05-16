n = int(input())
numbers = [int(input()) for _ in range(n)]

#bubble sort
# for i in range(n):
#     for j in range(0, n-i-1):
#         if numbers[j] > numbers[j+1]:
#             numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

#selection sort
# for i in range(n-1):
#     smallest_index = i
#     for j in range(i+1, n):
#         if numbers[smallest_index] > numbers[j]:
#             smallest_index = j
#     numbers[i], numbers[smallest_index] = numbers[smallest_index], numbers[i]

#insertion sort
# for i in range(1, n):
#     for j in range(i, 0, -1):
#         if numbers[j-1] > numbers[j]:
#             numbers[j-1], numbers[j] = numbers[j], numbers[j-1]

for num in numbers:
    print(num)
