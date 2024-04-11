from collections import deque

n, m = map(int, input().split())

board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

store = []
for _ in range(m):
    r, c = map(int, input().split())
    store.append([r-1, c-1])

people = [[-1, -1] for _ in range(m)]
visited = [[False] * n for _ in range(n)]

#     상  좌  우  하
dr = [-1, 0, 0, 1]
dc = [0, -1, 1, 0]

# start로 기준으로 최단거리 계산
def get_dist(start_r, start_c):
    queue = deque()
    queue.append([start_r, start_c])
    
    dist = [[-1] * n for _ in range(n)] # 방문 여부, 거리
    dist[start_r][start_c] = 0

    while queue:
        r, c = queue.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < n and 0 <= nc < n and \
                dist[nr][nc] == -1 and visited[nr][nc] == False:
                queue.append([nr, nc])
                dist[nr][nc] = dist[r][c] + 1
    
    return dist

def move_towards_store():
    for i in range(m):
        if people[i] == [-1, -1] or people[i] == store[i]:
            continue
        
        dist = get_dist(store[i][0], store[i][1])

        min_dist = int(1e9)
        people_r, people_c = -1, -1

        for d in range(4):
            nr = people[i][0] + dr[d]
            nc = people[i][1] + dc[d]
            if 0 <= nr < n and 0 <= nc < n and \
                dist[nr][nc] < min_dist and dist[nr][nc] != -1:
                min_dist = dist[nr][nc]
                people_r, people_c = nr, nc
        
        people[i] = [people_r, people_c]

def block_store_location():
    for i in range(m):
        if people[i] == store[i]:
            store_r, store_c = store[i]
            visited[store_r][store_c] = True

def enter_near_basecamp(idx):
    dist = get_dist(store[idx][0], store[idx][1])

    min_dist = int(1e9)
    people_r, people_c = -1, -1

    for r in range(n):
        for c in range(n):
            if board[r][c] == 1 and dist[r][c] < min_dist and dist[r][c] != -1:
                min_dist = dist[r][c]
                people_r, people_c = r, c
    
    people[idx] = [people_r, people_c]
    visited[people_r][people_c] = True

time = 0

while True:
    time += 1

    move_towards_store()
    block_store_location()
    if time <= m:
        enter_near_basecamp(time-1)
        
    # 모두 도착했는지 확인
    all_arrive = True
    for i in range(m):
        if people[i] != store[i]:
            all_arrive = False
            break

    if all_arrive == True:
        break

print(time)
