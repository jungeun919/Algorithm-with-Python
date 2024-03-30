# 0으로 시작 x
# 1 두 번 연속 x

# n | 경우의 수
# ===========
# 1 | 1
# 2 | 10
# 3 | 100 101
# 4 | 1010 1000 1001
# 5 | 10100 10101 10010 10000 10001

# dp[i] = dp[i-2] + dp[i-1]
# 10 + dp[i-2] / 10 + dp[i-1] (첫 번째 문자 제외)

n = int(input())

dp = [0] * (n + 1)
dp[1] = 1

for i in range(2, n + 1):
	dp[i] = dp[i-2] + dp[i-1]

print(dp[n])
