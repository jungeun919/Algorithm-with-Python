# dp[0] = 0
# dp[1] = P1
# dp[2] = max(dp[2], P2 + dp[2-0], P1 + dp[2-1])

N = int(input())
P = [0] + list(map(int, input().split())) # i개가 들어있는 카드팩의 금액

dp = [0] * (N+1) # i개가 들어있는 카드팩 구매시 금액의 최댓값

for i in range(1, N+1):
	for j in range(1, i+1):
		dp[i] = max(dp[i], P[j] + dp[i-j])

print(dp[N])
