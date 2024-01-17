# import sys

# input = sys.stdin.readline

# n, m = map(int, input().split())

# board = []
# for _ in range(n):
# 	board.append(list(map(int, input().split())))

# k = int(input())

# for _ in range(k):
# 	r1, c1, r2, c2 = map(int, input().split())

# 	total = 0
# 	# 인덱스 0부터 시작 (좌표는 1부터 시작)
# 	for r in range(r1-1, r2):
# 		total += sum(board[r][c1-1:c2])
# 	print(total)

import sys

input = sys.stdin.readline

n, m = map(int, input().split())

board = []
for _ in range(n):
	board.append(list(map(int, input().split())))

dp = [[0] * (m+1) for _ in range(n+1)]

for i in range(1, n+1):
	for j in range(1, m+1):
		dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + board[i-1][j-1]

k = int(input())

for _ in range(k):
	r1, c1, r2, c2 = map(int, input().split())
	print(dp[r2][c2] - dp[r2][c1-1] - dp[r1-1][c2] + dp[r1-1][c1-1])
