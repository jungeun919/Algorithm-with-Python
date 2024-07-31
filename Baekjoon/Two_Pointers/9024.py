import sys

input = sys.stdin.readline

T = int(input())

def get_comb(nums, K):
    nums.sort()

    left = 0
    right = len(nums) - 1
    min_diff = int(2e8)
    count = 0

    while left < right:
        temp = nums[left] + nums[right]
        diff = abs(temp - K)

        if min_diff > diff:
            min_diff = diff
            count = 1
        elif min_diff == diff:
            count += 1

        if temp == K:
            left += 1
            right -= 1
        elif temp < K:
            left += 1
        else:
            right -= 1

    return count

for _ in range(T):
    n, K = map(int, input().split())
    nums = list(map(int, input().split()))
    print(get_comb(nums, K))
