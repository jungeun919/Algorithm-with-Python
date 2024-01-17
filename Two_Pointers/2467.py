import sys

input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

left = 0
right = n - 1

res_sum = 2000000000
res_left = 0
res_right = 0

while left < right:
    temp = nums[left] + nums[right]
    if abs(temp) < res_sum:
        res_sum = abs(temp)
        res_left = nums[left]
        res_right = nums[right]
        
        if res_sum == 0:
            break
    
    if temp < 0:
        left += 1
    else:
        right -= 1

print(res_left, res_right)
