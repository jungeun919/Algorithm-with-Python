import sys

input = sys.stdin.readline

row, col = map(int, input().split())

board = []
for _ in range(row):
    board.append(list(input()))

#     상  하  좌  우
dy = [1, -1, 0, 0]
dx = [0, 0, -1, 1]

alpha = set(board[0][0])
res = 0

def dfs(y, x, count):
    global res
    
    res = max(res, count)
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= ny < row and 0 <= nx < col and board[ny][nx] not in alpha:
            alpha.add(board[ny][nx])
            dfs(ny, nx, count + 1)
            alpha.remove(board[ny][nx])

dfs(0, 0, 1)

print(res)
