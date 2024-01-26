n = int(input()) # 재료의 개수
m = int(input()) # 갑옷을 만드는데 필요한 수
nums = list(map(int, input().split()))

nums.sort()

left = 0
right = n - 1
count = 0

while left < right:
    total = nums[left] + nums[right]
    if total < m:
        left += 1
    elif total > m:
        right -= 1
    else:
        count += 1
        left += 1
        right -= 1

print(count)
