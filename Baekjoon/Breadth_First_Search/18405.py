from collections import deque
import sys

input = sys.stdin.readline

# K: 바이러스 종류(1~K번)
N, K = map(int, input().split())

board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

target_time, target_r, target_c = map(int, input().split())

virus = []
for r in range(N):
    for c in range(N):
        if board[r][c] != 0:
            virus.append([board[r][c], r, c, 0])


virus.sort()

#     상  하  좌  우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs():
    queue = deque(virus)

    while queue:
        virus_idx, r, c, time = queue.popleft()

        if time == target_time:
            break

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < N:
                if board[nr][nc] == 0: # 바이러스 존재하지 않을 경우
                    board[nr][nc] = virus_idx
                    queue.append([virus_idx, nr, nc, time+1])

bfs()
print(board[target_r-1][target_c-1])
