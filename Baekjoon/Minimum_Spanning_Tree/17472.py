from collections import deque
import sys

input = sys.stdin.readline
INF = int(1e9)

N, M = map(int, input().split())

board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

#     상  하  좌  우
dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]

def bfs(row, col, val, visited):
    queue = deque()
    queue.append([row, col])
    board[row][col] = val
    visited[row][col] = True

    while queue:
        r, c = queue.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < M:
                if board[nr][nc] != 0 and not visited[nr][nc]:
                    queue.append([nr, nc])
                    board[nr][nc] = val
                    visited[nr][nc] = True

def make_island():
    visited = [[False] * M for _ in range(N)]

    val = 1 # 섬 구분
    for row in range(N):
        for col in range(M):
            if board[row][col] == 1 and visited[row][col] == False:
                bfs(row, col, val, visited)
                val += 1
    return val-1 # 섬 개수

def get_dist(row, col, island): # 행, 열, 섬 인덱스
    for i in range(4): # 네 방향 각각 확인
        nr, nc = row, col
        connect_dist = 0

        while True: # 한 방향으로 이동
            nr += dr[i]
            nc += dc[i]

            if not (0 <= nr < N and 0 <= nc < M) or board[nr][nc] == island:
                break
            if board[nr][nc] != 0: # 다른 섬을 만남
                if connect_dist >= 2:
                    other_island = board[nr][nc]
                    dist[island-1][other_island-1] = min(dist[island-1][other_island-1], connect_dist)
                break
            connect_dist += 1

island_count = make_island()

dist = [[INF] * island_count for _ in range(island_count)]
for row in range(N):
    for col in range(M):
        if board[row][col] != 0:
            get_dist(row, col, board[row][col])

edges = []
for a in range(island_count):
    for b in range(a+1, island_count):
        if dist[a][b] != INF:
            edges.append([dist[a][b], a+1, b+1])
edges.sort()

parent = [i for i in range(island_count + 1)]

def find_parent(node):
    if node != parent[node]:
        parent[node] = find_parent(parent[node])
    return parent[node]

def union_parent(x, y):
    root_x = find_parent(x)
    root_y = find_parent(y)
    if root_x != root_y:
        parent[root_y] = root_x

connect_bridge = 0
res = 0

while edges:
    dist, a, b = edges.pop(0)

    if find_parent(a) != find_parent(b):
        union_parent(a, b)
        connect_bridge += 1
        res += dist

    if connect_bridge == island_count - 1:
        break

if connect_bridge == island_count - 1:
    print(res)
else:
    print(-1)
