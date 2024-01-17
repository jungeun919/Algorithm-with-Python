from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

graph = []

for _ in range(n):
    graph.append(list(map(int, input().rstrip())))
    
#     상  하  좌  우
dy = [1, -1, 0, 0]
dx = [0, 0, -1, 1]

def bfs(y, x):
    queue = deque()
    queue.append((y, x))
    
    while queue:
        y, x = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or ny < 0 or nx >= m or ny >= n:
                continue
            
            if graph[ny][nx] == 1:
                queue.append((ny, nx))
                graph[ny][nx] = graph[y][x] + 1
            
bfs(0, 0)

print(graph[n - 1][m - 1])
