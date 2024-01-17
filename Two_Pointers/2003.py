import sys

input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))

start = 0
end = 1
count = 0

while start <= end and end <= n:
    temp = sum(nums[start:end])
    if temp < m:
        end += 1
    elif temp > m:
        start += 1
    else:
        count += 1
        start += 1

print(count)
