from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

# . | 빈 칸
# # | 벽
# O | 구멍
board = []
for _ in range(n):
	board.append(list(input().rstrip()))

for r in range(n):
	for c in range(m):
		if board[r][c] == 'R':
			rx, ry = r, c
		if board[r][c] == 'B':
			bx, by = r, c

#     상  하  좌  우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def move(x, y, dx, dy): # 해당 방향으로 이동
	count = 0

	while True:
		# 다음이 벽이거나 현재가 구멍일 때까지
		if board[x+dx][y+dy] == '#' or board[x][y] == 'O':
			return x, y, count
		
		# 구슬 이동
		x += dx
		y += dy
		count += 1

def bfs(rx, ry, bx, by):
	queue = deque()
	queue.append([rx, ry, bx, by, 0])

	visited[rx][ry][bx][by] = True

	while queue:
		rx, ry, bx, by, count = queue.popleft()

		if count > 10:
			print(-1)
			return
		
		if board[rx][ry] == 'O':
			print(count)
			return
		
		for i in range(4):
			nrx, nry, rcount = move(rx, ry, dx[i], dy[i])
			nbx, nby, bcount = move(bx, by, dx[i], dy[i])

			if board[nbx][nby] == 'O':
				continue
				
			if nrx == nbx and nry == nby: # 위치가 겹쳤을때
				if rcount > bcount: # 이동거리가 많은 쪽이 뒤로 한칸 이동
					nrx -= dx[i]
					nry -= dy[i]
				else:
					nbx -= dx[i]
					nby -= dy[i]
			
			if visited[nrx][nry][nbx][nby] == False:
				visited[nrx][nry][nbx][nby] = True
				queue.append([nrx, nry, nbx, nby, count + 1])
	
	print(-1)

visited = [[[[False] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]
bfs(rx, ry, bx, by)
