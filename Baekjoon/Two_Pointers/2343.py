import sys

input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))

left = max(nums) # 블루레이의 최소 크기
right = sum(nums) # 블루레이의 최대 크기

while left <= right:
    mid = (left + right) // 2
    
    # 블루레이의 크기를 mid로 했을 때 그룹 개수
    group = 0
    sum = 0
    for i in range(n):
        if sum + nums[i] > mid: # 현재 블루레이 크기 초과시
            group += 1
            sum = 0
        sum += nums[i]
    if sum != 0:
        group += 1
    
    if group > m:
        left = mid + 1
    else:
        right = mid - 1

print(left)
