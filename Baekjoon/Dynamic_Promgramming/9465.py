import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
	n = int(input()) # 2 * n
	sticker = []
	for _ in range(2):
		sticker.append(list(map(int, input().split())))
	
	# dp[0][i]: i열까지 봤을 경우, 0행 i열을 마지막으로 선택
	# dp[1][i]: i얄까지 봤을 경우, 1행 i열을 마지막으로 선택
	dp = [[0] * n for _ in range(2)]

	dp[0][0] = sticker[0][0]
	dp[1][0] = sticker[1][0]
	if n == 1:
		print(max(dp[0][0], dp[1][0]))
		continue

	dp[0][1] = sticker[1][0] + sticker[0][1]
	dp[1][1] = sticker[0][0] + sticker[1][1]
	if n == 2:
		print(max(dp[0][1], dp[1][1]))
		continue
	
	for i in range(2, n):
		dp[0][i] = max(dp[1][i-2], dp[1][i-1]) + sticker[0][i]
		dp[1][i] = max(dp[0][i-2], dp[0][i-1]) + sticker[1][i]
	print(max(dp[0][n-1], dp[1][n-1]))
