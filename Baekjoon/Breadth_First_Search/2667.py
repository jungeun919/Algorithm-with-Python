from collections import deque
import sys

input = sys.stdin.readline

n = int(input())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().rstrip())))

#     상  하  좌  우
dy = [1, -1, 0, 0]
dx = [0, 0, -1, 1]

def bfs(y, x): # row, col
    queue = deque()
    queue.append((y, x))
    graph[y][x] = 0
    count = 1
    
    while queue:
        y, x = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            
            if graph[ny][nx] == 1:
                graph[ny][nx] = 0
                queue.append((ny, nx))
                count += 1
                
    return count

count = []

for row in range(n):
    for col in range(n):
        if graph[row][col] == 1:
            value = bfs(row, col)
            count.append(value)

count.sort()

print(len(count))
for i in count:
    print(i)
