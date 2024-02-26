from collections import deque
import sys

input = sys.stdin.readline

board = []
for _ in range(12):
    board.append(list(input().rstrip()))

#     상  하  좌  우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(r, c):
    queue = deque()
    queue.append([r, c])
    visited[r][c] = True

    around_pos = []
    around_pos.append([r, c])
    
    while queue:
        y, x = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= ny < 12 and 0 <= nx < 6 and \
                board[ny][nx] == board[y][x] and visited[ny][nx] == False:
                queue.append([ny, nx])
                visited[ny][nx] = True
                around_pos.append([ny, nx])

    return around_pos

def down(bomb_pos):
    for r, c in bomb_pos:
        for i in range(r, 0, -1):
            board[i][c] = board[i-1][c]
        board[0][c] = '.'

chain = 0
while True:
    visited = [[False] * 6 for _ in range(12)]
    bomb_pos = []

    for r in range(12):
        for c in range(6):
            if board[r][c] != '.' and visited[r][c] == False:
                around_pos = bfs(r, c)

                if len(around_pos) >= 4:
                    around_pos.sort(key=lambda x: (x[0], x[1]))
                    for y, x in around_pos:
                        board[y][x] = '.'
                        bomb_pos.append([y, x])

    if len(bomb_pos) == 0:
        break

    down(bomb_pos)
    chain += 1
print(chain)
