from collections import deque

n = int(input())

board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

robot_level = 2
robot_r, robot_c = -1, -1
for r in range(n):
    for c in range(n):
        if board[r][c] == 9:
            robot_r, robot_c = r, c
            board[r][c] = 0

#     상  하  좌  우
dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]

def search_monster(robot_r, robot_c):
    queue = deque() # 로봇 이동
    queue.append([robot_r, robot_c])

    visited = [[-1] * n for _ in range(n)] # 방문 여부, 거리 저장
    visited[robot_r][robot_c] = 0

    candidate = []

    while queue:
        r, c = queue.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < n and 0 <= nc < n and \
                visited[nr][nc] == -1 and board[nr][nc] <= robot_level:
                visited[nr][nc] = visited[r][c] + 1
                queue.append([nr, nc])
                if 1 <= board[nr][nc] < robot_level:
                    candidate.append([visited[nr][nc], nr, nc])
    
    candidate.sort()
    
    if candidate:
        return candidate[0]
    return None

time = 0
remove_count = 0

while True:
    monster = search_monster(robot_r, robot_c)
    if monster == None:
        break
    
    move_dist, robot_r, robot_c = monster
    time += move_dist
    board[robot_r][robot_c] = 0
    remove_count += 1

    if remove_count == robot_level:
        robot_level += 1
        remove_count = 0

print(time)
