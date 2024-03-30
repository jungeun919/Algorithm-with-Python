x = int(input())
dp = [0] * (x + 1) # 연산 횟수
path = [""] * (x + 1) # 경로
path[1] = "1"

for i in range(2, x + 1):
	dp[i] = dp[i - 1] + 1
	prev = i - 1

	if i % 3 == 0 and dp[i // 3] + 1 < dp[i]:
		dp[i] = dp[i // 3] + 1
		prev = i // 3
	
	if i % 2 == 0 and dp[i // 2] + 1 < dp[i]:
		dp[i] = dp[i // 2] + 1
		prev = i // 2
	
	path[i] = str(i) + " " + path[prev]

print(dp[x])
print(path[x])
