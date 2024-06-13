from collections import deque
import sys

input = sys.stdin.readline

K = int(input()) # 말처럼 이동가능한 횟수
W, H = map(int, input().split())

# 0 (평지) / 1 (장애물)
board = []
for _ in range(H):
    board.append(list(map(int, input().split())))

# 원숭이 이동 방향
mdr = [-1, 1, 0, 0]
mdc = [0, 0, -1, 1]

# 말 이동 방향
hdr = [-2, -2, -1, -1, 1, 1, 2, 2]
hdc = [-1, 1, -2, 2, -2, 2, -1, 1]

def bfs():
    queue = deque()
    queue.append([0, 0, K])

    # visited[행][열][말처럼 이동가능한 횟수]
    visited = [[[-1] * (K+1) for _ in range(W)] for _ in range(H)]
    visited[0][0][K] = 0

    while queue:
        r, c, k = queue.popleft()

        if r == H-1 and c == W-1:
            return visited[r][c][k]

        if k > 0:
            for d in range(8):
                nr = r + hdr[d]
                nc = c + hdc[d]
                if 0 <= nr < H and 0 <= nc < W:
                    if board[nr][nc] != 1 and visited[nr][nc][k-1] == -1:
                        visited[nr][nc][k-1] = visited[r][c][k] + 1
                        queue.append([nr, nc, k-1])

        for d in range(4):
            nr = r + mdr[d]
            nc = c + mdc[d]
            if 0 <= nr < H and 0 <= nc < W:
                if board[nr][nc] != 1 and visited[nr][nc][k] == -1:
                    visited[nr][nc][k] = visited[r][c][k] + 1
                    queue.append([nr, nc, k])

    return -1

print(bfs())
