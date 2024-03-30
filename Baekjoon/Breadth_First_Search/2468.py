from collections import deque
import sys

input = sys.stdin.readline

n = int(input())

max_height = 0
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))
    max_height = max(max_height, max(graph[i]))

def bfs(y, x, value):
    #     상  하  좌  우
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    
    queue = deque()
    queue.append([y, x])
    visited[y][x] = True
    
    while queue:
        y, x = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= ny < n and 0 <= nx < n and \
                graph[ny][nx] > value and visited[ny][nx] == False:
                queue.append([ny, nx])
                visited[ny][nx] = True

res_safe = []

for i in range(max_height):
    visited = [[False] * n for _ in range(n)]
    
    safe = 0
    for row in range(n):
        for col in range(n):
            if graph[row][col] > i and visited[row][col] == False:
                bfs(row, col, i)
                safe += 1
    
    res_safe.append(safe)

print(max(res_safe))
