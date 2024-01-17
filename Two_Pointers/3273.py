import sys

input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
x = int(input())

nums.sort()

count = 0
left = 0
right = n - 1

while left < right:
    temp = nums[left] + nums[right]
    if temp == x:
        count += 1
    
    if temp < x:
        left += 1
    else:
        right -= 1

print(count)
