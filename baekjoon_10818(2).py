n = int(input())
nums = list(map(int, input().split()))

smallest = biggest = nums[0]
for num in nums:
    if num < smallest:
        smallest = num
    if num > biggest:
        biggest = num

print(smallest, biggest)