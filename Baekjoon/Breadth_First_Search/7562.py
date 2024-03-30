from collections import deque
import sys

input = sys.stdin.readline

dx = [-2, -1, 1, 2, -2, -1, 1, 2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]

def bfs(start_x, start_y, end_x, end_y):
    queue = deque()
    queue.append([start_x, start_y])
    graph[start_x][start_y] = 1
    
    while queue:
        x, y = queue.popleft()
        
        if x == end_x and y == end_y:
            print(graph[x][y] - 1)
            return
    
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < length and 0 <= ny < length and graph[nx][ny] == 0:
                queue.append([nx, ny])
                graph[nx][ny] = graph[x][y] + 1

T = int(input())

for _ in range(T):
    length = int(input())
    start_x, start_y = map(int, input().split())
    end_x, end_y = map(int, input().split())
    
    graph = [[0] * length for _ in range(length)]
    
    bfs(start_x, start_y, end_x, end_y)
