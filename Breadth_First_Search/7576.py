from collections import deque
import sys

input = sys.stdin.readline

m, n = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

#     상  하  좌  우
dy = [1, -1, 0, 0]
dx = [0, 0, -1, 1]

queue = deque()

for row in range(n):
    for col in range(m):
        if graph[row][col] == 1:
            queue.append([row, col])

def bfs():
    while queue:
        y, x = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < m and 0 <= ny < n and graph[ny][nx] == 0:
                graph[ny][nx] = graph[y][x] + 1
                queue.append([ny, nx])
                
bfs()

count = 0

for row in graph:
    for col in row:
        if col == 0:
            print(-1)
            exit(0)
    count = max(count, max(row))
    
print(count - 1)
