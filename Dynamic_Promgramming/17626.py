import math

n = int(input())
dp = [0, 1]

for i in range(2, n + 1):
	min_val = int(1e9)
	for j in range(1, int(math.sqrt(i)) + 1):
		min_val = min(min_val, dp[i - j**2] + 1)
	dp.append(min_val)

print(dp[n])
