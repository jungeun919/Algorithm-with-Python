from collections import deque

#     상  하  좌  우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(n, m, land, visited, oil, r, c):
    queue = deque()
    queue.append([r, c])
    visited[r][c] = True
    
    count = 0
    visited_col = {c} # set 중복 제거
    
    while queue:
        r, c = queue.popleft()
        count += 1
        visited_col.add(c)
        
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            
            if not(0 <= nr < n and 0 <= nc < m):
                continue
            if land[nr][nc] == 1 and visited[nr][nc] == False:
                queue.append([nr, nc])
                visited[nr][nc] = True
    
    for col in visited_col:
        oil[col] += count

def solution(land):
    n = len(land)
    m = len(land[0])
    
    oil = [0] * m # 시추관의 위치가 idx일 경우 획득할 석유량
    visited = [[False] * m for _ in range(n)]

    for r in range(n):
        for c in range(m):
            if land[r][c] == 1 and visited[r][c] == False:
                bfs(n, m, land, visited, oil, r, c)
    
    return max(oil)
