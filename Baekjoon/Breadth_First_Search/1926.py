from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

def bfs(y, x):
    #     상  하  좌  우
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]

    queue = deque()
    queue.append([y, x])
    board[y][x] = 0
    area = 1
    
    while queue:
        y, x = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= ny < n and 0 <= nx < m and board[ny][nx] == 1:
                queue.append([ny, nx])
                board[ny][nx] = 0
                area += 1
    return area

count = 0
max_area = 0
for row in range(n):
    for col in range(m):
        if board[row][col] == 1:
            area = bfs(row, col)
            count += 1
            max_area = max(max_area, area)

print(count)
print(max_area)
