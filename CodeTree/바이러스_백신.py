from collections import deque

INF = int(1e9)

n, m = map(int, input().split())

board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

hospital = []
for r in range(n):
    for c in range(n):
        if board[r][c] == 2:
            hospital.append([r, c])

#     상  하  좌  우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def get_comb(arr: list, start_idx: int):
    if len(arr) == m:
        hospital_comb.append(arr[:])
        return
    
    for idx in range(start_idx, len(hospital)):
        arr.append(hospital[idx])
        get_comb(arr, idx + 1)
        arr.pop()

def get_time_to_kill_all_virus(comb: list):
    visited = [[False] * n for _ in range(n)]
    time = [[0] * n for _ in range(n)]

    queue = deque()

    for hospital in comb:
        visited[hospital[0]][hospital[1]] = True
        queue.append([hospital[0], hospital[1]])
    
    while queue:
        y, x = queue.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < n and 0 <= nx < n and \
                board[ny][nx] != 1 and visited[ny][nx] == False: # 1: 벽
                visited[ny][nx] = True
                time[ny][nx] = time[y][x] + 1
                queue.append([ny, nx])
    
    max_time = 0
    for r in range(n):
        for c in range(n):
            if board[r][c] == 0: # 0: 바이러스
                if visited[r][c] == False:
                    return INF
                else:
                    max_time = max(max_time, time[r][c])
    return max_time

hospital_comb = []
get_comb([], 0)

min_time = INF
for comb in hospital_comb:
    time = get_time_to_kill_all_virus(comb)
    min_time = min(min_time, time)

if min_time == INF:
    print(-1)
else:
    print(min_time)
