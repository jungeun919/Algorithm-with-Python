from collections import deque
import sys

input = sys.stdin.readline

n = int(input())

board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

shark_size = 2
shark_y, shark_x = -1, -1
for r in range(n):
    for c in range(n):
        if board[r][c] == 9:
            shark_y, shark_x = r, c
            board[r][c] = 0

#     상  하  좌  우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(shark_y, shark_x):
    queue = deque()
    queue.append([shark_y, shark_x])

    candidate = []

    visited = [[-1] * n for _ in range(n)] # 방문 여부, 거리 저장
    visited[shark_y][shark_x] = 0

    while queue:
        y, x = queue.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < n and 0 <= nx < n and visited[ny][nx] == -1:
                if board[ny][nx] <= shark_size:
                    visited[ny][nx] = visited[y][x] + 1
                    queue.append([ny, nx])

                    if 0 < board[ny][nx] < shark_size:
                        candidate.append([visited[ny][nx], ny, nx])

    candidate.sort()

    if candidate:
        return candidate[0]
    return None

time = 0
size = 0

while True:
    fish = bfs(shark_y, shark_x)

    if fish is None:
        break

    time += fish[0]
    shark_y, shark_x = fish[1], fish[2]
    board[shark_y][shark_x] = 0
    size += 1

    if size == shark_size:
        shark_size += 1
        size = 0

print(time)


# from collections import deque
# import sys
#
# input = sys.stdin.readline
#
# n = int(input())
#
# board = []
# for _ in range(n):
#     board.append(list(map(int, input().split())))
#
# shark_size = 2
# shark_y, shark_x = -1, -1
# for r in range(n):
#     for c in range(n):
#         if board[r][c] == 9:
#             shark_y, shark_x = r, c
#             board[r][c] = 0
#
# #     상  하  좌  우
# dx = [0, 0, -1, 1]
# dy = [-1, 1, 0, 0]
#
# def bfs(shark_y, shark_x):
#     queue = deque()
#     queue.append([shark_y, shark_x])
#
#     visited = [[-1] * n for _ in range(n)] # 방문 여부, 거리 저장
#     visited[shark_y][shark_x] = 0
#
#     while queue:
#         y, x = queue.popleft()
#
#         for i in range(4):
#             ny = y + dy[i]
#             nx = x + dx[i]
#
#             if 0 <= ny < n and 0 <= nx < n and \
#                 shark_size >= board[ny][nx] and visited[ny][nx] == -1:
#                 queue.append([ny, nx])
#                 visited[ny][nx] = visited[y][x] + 1
#
#     return visited
#
# def find_fish_to_eat(visited):
#     candidate = []
#
#     for r in range(n):
#         for c in range(n):
#             if visited[r][c] != -1 and 1 <= board[r][c] < shark_size:
#                 candidate.append([visited[r][c], r, c])
#
#     # candidate.sort(key=lambda x: [x[0], x[1], x[2]]) # 거리, 위, 왼쪽 순으로
#     candidate.sort()
#
#     if candidate:
#         return candidate[0]
#     return None
#
# time = 0
# size = 0
#
# while True:
#     visited = bfs(shark_y, shark_x)
#     fish = find_fish_to_eat(visited)
#
#     if fish is None:
#         break
#
#     time += fish[0]
#     shark_y, shark_x = fish[1], fish[2]
#     board[shark_y][shark_x] = 0
#     size += 1
#
#     if size == shark_size:
#         shark_size += 1
#         size = 0
#
# print(time)
