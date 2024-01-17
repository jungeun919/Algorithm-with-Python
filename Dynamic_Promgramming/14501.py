import sys

input = sys.stdin.readline

n = int(input())

schedule = [] # [상담 기간, 금액]
for _ in range(n):
	schedule.append(list(map(int, input().split())))

dp = [0] * (n + 1)

for i in range(n): # i번째까지 일했을 떄 얻는 수익 (0~6)
	for j in range(i + schedule[i][0], n + 1):
		if dp[j] < dp[i] + schedule[i][1]:
			dp[j] = dp[i] + schedule[i][1]

print(dp[n])
