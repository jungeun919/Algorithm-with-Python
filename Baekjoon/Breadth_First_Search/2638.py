from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

#     상  하  좌  우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs():
    queue = deque() # 공기
    queue.append([0, 0])

    visited = [[0] * m for _ in range(n)] # 공기 방문 여부
    visited[0][0] = True

    melt = [[0] * m for _ in range(n)] # 공기와 접촉된 횟수

    while queue:
        y, x = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= ny < n and 0 <= nx < m and visited[ny][nx] == False:
                if board[ny][nx] == 0:
                    visited[ny][nx] = True
                    queue.append([ny, nx])
                elif board[ny][nx] == 1:
                    melt[ny][nx] += 1

    melt_count = 0
    for r in range(n):
        for c in range(m):
            if melt[r][c] >= 2:
                board[r][c] = 0
                melt_count += 1
    return melt_count

# 초기 치즈 개수 계산
cheese_count = 0
for r in range(n):
    for c in range(m):
        if board[r][c] == 1:
            cheese_count += 1

time = 0
while cheese_count > 0:
    melt_count = bfs()
    time += 1
    cheese_count -= melt_count
print(time)
