# 4*4 board 구성
# (0,0) (0,1) (0,2) (0,3)
# (1,0) (1,1) (1,2) (1,3)
# (2,0) (2,1) (2,2) (2,3)
# (3,0) (3,1) (3,2) (3,3)

import sys

input = sys.stdin.readline

N, M, K = map(int, input().split())

board = []
for _ in range(N):
    board.append(list(input().rstrip()))

# 해당 색상으로 보드를 구성할 때 최소 변경 횟수
def count_board_change(color):
    dp = [[0] * (M + 1) for _ in range(N + 1)]

    for i in range(N):
        for j in range(M):
            if (i+j) % 2 == 0: # 시작 칸과 동알한 색으로 구성된 칸
                val = board[i][j] != color # True이면 0, False면 1 반환
            else: # 시작 칸과 다른 색으로 구성된 칸
                val = board[i][j] == color
            dp[i+1][j+1] = val + dp[i+1][j] + dp[i][j+1] - dp[i][j]

    min_count = (N*M) // 2
    for i in range(1, N-K+2):
        for j in range(1, M-K+2):
            min_count = min(min_count, dp[i+K-1][j+K-1] - dp[i+K-1][j-1] - dp[i-1][j+K-1] + dp[i-1][j-1])
    return min_count

print(min(count_board_change('B'), count_board_change('W')))
