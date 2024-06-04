from collections import deque
import sys

input = sys.stdin.readline

# (#) 지나갈 수 없음
# (.) 빈 칸
# (S) 시작 지점
# (E) 출구

df = [1, -1, 0, 0, 0, 0]
dr = [0, 0, 1, -1, 0, 0]
dc = [0, 0, 0, 0, 1, -1]

def bfs(floor, r, c):
    queue = deque()
    queue.append([floor, r, c])

    visited = [[[-1] * C for _ in range(R)] for _ in range(L)] # 방문 여부, 시간 저장
    visited[floor][r][c] = 0

    while queue:
        floor, r, c = queue.popleft()

        for d in range(6):
            nf = floor + df[d]
            nr = r + dr[d]
            nc = c + dc[d]

            if 0 <= nf < L and 0 <= nr < R and 0 <= nc < C:
                if board[nf][nr][nc] == 'E':
                    print(f"Escaped in {visited[floor][r][c] + 1} minute(s).")
                    return
                if board[nf][nr][nc] == '.' and visited[nf][nr][nc] == -1:
                    queue.append([nf, nr, nc])
                    visited[nf][nr][nc] = visited[floor][r][c] + 1

    print("Trapped!")

while True:
    L, R, C = map(int, input().split()) # 층 수, 행, 열

    if L == R == C == 0:
        break

    board = []
    for _ in range(L):
        board.append([list(input()) for _ in range(R)])
        input() # 줄바꿈

    for floor in range(L):
        for r in range(R):
            for c in range(C):
                if board[floor][r][c] == 'S':
                    bfs(floor, r, c)
