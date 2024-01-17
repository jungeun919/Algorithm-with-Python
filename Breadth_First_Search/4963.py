# 1 : 섬
# 0 : 바다
# 섬의 개수 구하기

from collections import deque
import sys

input = sys.stdin.readline

def bfs(y, x):
    # 상 하 좌 우 대각선 4방향
    dx = [-1, 0, 1, 1, 1, 0, -1, -1]
    dy = [1, 1, 1, 0, -1, -1, -1, 0]
    
    queue = deque()
    queue.append([y, x])
    graph[y][x] = 0
    
    while queue:
        y, x = queue.popleft()
                
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= ny < height and 0 <= nx < width and graph[ny][nx] == 1:
                queue.append([ny, nx])
                graph[ny][nx] = 0

while True:
    width, height = map(int, input().split())
    
    if width == height == 0:
        break
    
    graph = []
    for _ in range(height):
        graph.append(list(map(int, input().split())))
    
    count = 0
    for row in range(height):
        for col in range(width):
            if graph[row][col] == 1:
                bfs(row, col)
                count += 1
    print(count)
