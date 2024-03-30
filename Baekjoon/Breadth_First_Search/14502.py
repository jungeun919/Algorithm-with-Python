# 0 : 빈 칸
# 1 : 벽
# 2 : 바이러스
# 벽 3개 설치

from collections import deque
import copy
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))

#     상  하  좌  우
dy = [1, -1, 0, 0]
dx = [0, 0, -1, 1]

def bfs():
    global safe_area
    
    queue = deque()
    
    temp_graph = copy.deepcopy(graph)
    for row in range(n):
        for col in range(m):
            if temp_graph[row][col] == 2:
                queue.append((row, col))
    
    while queue:
        y, x = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or ny < 0 or nx >= m or ny >= n:
                continue
            
            if temp_graph[ny][nx] == 0:
                temp_graph[ny][nx] = 2
                queue.append((ny, nx))
    
    count = 0
    for row in range(n):
        count += temp_graph[row].count(0)
    safe_area = max(safe_area, count)

def wall(count):
    if count == 3:
        bfs()
        return
    
    for row in range(n):
        for col in range(m):
            if graph[row][col] == 0:
                graph[row][col] = 1
                wall(count + 1)
                graph[row][col] = 0

safe_area = 0
wall(0)
print(safe_area)
