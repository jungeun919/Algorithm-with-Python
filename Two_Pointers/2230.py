import sys

input = sys.stdin.readline

n, m = map(int, input().split())

nums = []
for _ in range(n):
    nums.append(int(input()))

nums.sort()

left = 0
right = 0
min_diff = int(2e9)

while right < n:
    diff = nums[right] - nums[left]
    if diff == m:
        min_diff = m
        break
    elif diff < m:
        right += 1
    elif diff > m:
        left += 1
        min_diff = min(min_diff, diff)

print(min_diff)
