import sys

input = sys.stdin.readline

N = int(input())

board = []
for _ in range(N):
	board.append(list(map(int, input().split())))

dp = [[0] * N for _ in range(N)] # (r, c)까지 가는 경로 개수
dp[0][0] = 1

for r in range(N):
	for c in range(N):
		if r == N-1 and c == N-1:
			print(dp[r][c])
			break

		move = board[r][c]
		if c + move < N: # 오른쪽 이동
			dp[r][c + move] += dp[r][c]
		if r + move < N: # 아래 이동
			dp[r + move][c] += dp[r][c]
