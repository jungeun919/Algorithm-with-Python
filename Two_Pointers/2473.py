import sys

input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

nums.sort()

res_sum = 3000000000
res_num = [] # fix, left, right

for i in range(n - 2):
    fix = nums[i]
    left = i + 1
    right = n - 1
    
    while left < right:
        temp = fix + nums[left] + nums[right]
        if abs(temp) < res_sum:
            res_sum = abs(temp)
            res_num = [fix, nums[left], nums[right]]
        
            if temp == 0:
                break
        
        if temp < 0:
            left += 1
        else:
            right -= 1

print(res_num[0], res_num[1], res_num[2])
