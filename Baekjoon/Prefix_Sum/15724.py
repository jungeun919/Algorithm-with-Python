import sys

input = sys.stdin.readline

N, M = map(int, input().split())

board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

dp = [[0] * (M+1) for _ in range(N+1)]

for r in range(1, N+1):
    for c in range(1, M+1):
        dp[r][c] = board[r-1][c-1] + dp[r-1][c] + dp[r][c-1] - dp[r-1][c-1]

K = int(input())
for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    print(dp[x2][y2] - dp[x1-1][y2] - dp[x2][y1-1] + dp[x1-1][y1-1])
