import sys

input = sys.stdin.readline

N, M, K = map(int, input().split())

board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

#     상  하  좌  우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 아래, 오른쪽으로만 이동 가능
def dfs(start_r, start_c, count, sum):
    global max_sum

    if count == K:
        max_sum = max(max_sum, sum)
        return

    for r in range(start_r, N):
        for c in range(start_c if r == start_r else 0, M):
            if visited[r][c] == False:
                flag = False # 상하좌우에 방문했는지 여부
                for d in range(4):
                    nr = r + dr[d]
                    nc = c + dc[d]
                    if 0 <= nr < N and 0 <= nc < M and visited[nr][nc] == True:
                        flag = True

                if flag == False: # 인접하지 않은 경우
                    visited[r][c] = True
                    dfs(r, c, count+1, sum + board[r][c])
                    visited[r][c] = False

max_sum = -int(1e6)
visited = [[False] * M for _ in range(N)]
dfs(0, 0, 0, 0)
print(max_sum)
