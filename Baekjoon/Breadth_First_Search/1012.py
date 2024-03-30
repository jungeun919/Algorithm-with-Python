# m : 가로, n : 세로, k : 심은 배추 위치 개수
from collections import deque
import sys

input = sys.stdin.readline

T = int(input())

#     상  하  좌  우
dy = [1, -1, 0, 0]
dx = [0, 0, -1, 1]

def bfs(y, x, y_size, x_size):
    queue = deque()
    queue.append((y, x))
    graph[y][x] = 0
    
    while queue:
        y, x = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or ny < 0 or nx >= x_size or ny >= y_size:
                continue
            
            if graph[ny][nx] == 1:
                graph[ny][nx] = 0
                queue.append((ny, nx))

for _ in range(T):
    m, n, k = map(int, input().split())
    
    graph = [[0 for _ in range(m)] for _ in range(n)]
    
    for _ in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1
        
    count = 0
    for row in range(n):
        for col in range(m):
            if graph[row][col] == 1:
                bfs(row, col, n, m)
                count += 1
    print(count)
