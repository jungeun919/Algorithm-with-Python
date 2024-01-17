from collections import deque
import sys

input = sys.stdin.readline

# 가로, 세로, 높이
m, n, h = map(int, input().split())

graph = []

queue = deque()

# [height][row][col]
# [z][x][y]
for height in range(h):
    temp = []
    for row in range(n):
        temp.append(list(map(int, input().split())))
        for col in range(m):
            if temp[row][col] == 1:
                queue.append([height, row, col])
    graph.append(temp)
        
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

while queue:
    z, x, y = queue.popleft()
    
    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]
        nz = z + dz[i]
        
        if 0 <= nx < n and \
		    0 <= ny < m and \
            0 <= nz < h and \
            graph[nz][nx][ny] == 0:
            queue.append([nz, nx, ny])
            graph[nz][nx][ny] = graph[z][x][y] + 1

count = 0

for height in graph:
    for row in height:
        for col in row:
            if col == 0:
                print(-1)
                exit(0)
        count = max(count, max(row))
        
print(count - 1)
