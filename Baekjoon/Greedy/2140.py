import sys

input = sys.stdin.readline

N = int(input())

board = []
for _ in range(N):
    board.append(list(input()))

dr = [-1, -1, -1, 0, 0, 1, 1, 1]
dc = [-1, 0, 1, -1, 1, -1, 0, 1]

def check_bomb(r, c, count):
    for d in range(8):
        nr = r + dr[d]
        nc = c + dc[d]

        if not (0 <= nr < N and 0 <= nc < N):
            continue

        if board[nr][nc] == '#':
            if count > 0:
                board[nr][nc] = '*' # 지뢰 표시
            else:
                board[nr][nc] = 'X' # 지뢰 넣을 수 없음

        if board[nr][nc] == '*':
            count -= 1

for r in range(N):
    for c in range(N):
        if board[r][c].isdigit():
            check_bomb(r, c, int(board[r][c]))

res = 0
for r in range(N):
    for c in range(N):
        if board[r][c] == '*' or board[r][c] == '#':
            res += 1
print(res)
