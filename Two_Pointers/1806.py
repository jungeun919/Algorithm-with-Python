import sys

input = sys.stdin.readline

n, s = map(int, input().split())
nums = list(map(int, input().split()))

left = 0
right = 0

sum = nums[0]
length = 100000

while True:
    if sum >= s:
        length = min(length, right - left + 1)
        sum -= nums[left]
        left += 1
    
    else:
        right += 1
        if right == n:
            break
        sum += nums[right]

if length == 100000:
    print(0)
else:
    print(length)
