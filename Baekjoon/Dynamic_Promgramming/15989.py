# 1, 2로 구성
# 1 -> (1) 1개
# 2 -> (1,1) (2) 2개
# 3 -> (1,1,1) (1,2) 2개
# 4 -> (1,1,1,1) (1,1,2) (2,2) 3개
# 5 -> (1,1,1,1,1) (1,1,1,2) (1,2,2) 3개

T = int(input())

dp = [1] * 10001

for i in range(2, 10001):
	dp[i] += dp[i - 2]

for i in range(3, 10001):
	dp[i] += dp[i - 3]

for _ in range(T):
	n = int(input())
	print(dp[n])
