n = int(input())
nums = list(map(int, input().split()))

dp = [1] * n

for right in range(1, n):
	for left in range(right):
		if nums[right] > nums[left]:
			dp[right] = max(dp[right], dp[left] + 1)

print(max(dp))
