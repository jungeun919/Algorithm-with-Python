n, start, max = map(int, input().split())
volumes = list(map(int, input().split()))

dp = [[0] * (max + 1) for _ in range(n + 1)]
dp[0][start] = 1

for i in range(n):
	for j in range(max + 1):
		if dp[i][j] == 1:
			if j + volumes[i] <= max:
				dp[i + 1][j + volumes[i]] = 1
			if j - volumes[i] >= 0:
				dp[i + 1][j - volumes[i]] = 1

res = -1
for i in range(max + 1):
	if dp[n][i] == 1:
		res = i
print(res)
