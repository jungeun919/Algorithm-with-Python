from collections import deque
import sys

input = sys.stdin.readline

n = int(input())

board = []
for _ in range(n):
	board.append(list(map(int, input().split())))

visited = [[0] * n for _ in range(n)]

def bfs(row, col, val):
	#     상  하  좌  우
	dx = [0, 0, -1, 1]
	dy = [1, -1, 0, 0]

	queue = deque()
	queue.append([row, col, val])
	board[row][col] = val
	visited[row][col] = 1

	while queue:
		y, x, val = queue.popleft()

		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]

			if 0 <= nx < n and 0 <= ny < n and board[ny][nx] == 1:
				board[ny][nx] = val
				visited[row][col] = 1
				queue.append([ny, nx, val])

val = 2
for row in range(n):
	for col in range(n):
		if board[row][col] == 1 and visited[row][col] == 0:
			bfs(row, col, val)
			val += 1

def connect_land(val):
	#     상  하  좌  우
	dx = [0, 0, -1, 1]
	dy = [1, -1, 0, 0]

	dist = [[-1] * n for _ in range(n)]

	queue = deque()
	for row in range(n):
		for col in range(n):
			if board[row][col] == val:
				dist[row][col] = 0
				queue.append([row, col])
	
	while queue:
		y, x = queue.popleft()

		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]

			if 0 <= nx < n and 0 <= ny < n:
				# 육지고, 다른 섬일 경우
				if board[ny][nx] != 0 and board[ny][nx] != val:
					return dist[y][x]
				# 바다고, 아직 다리가 연결되지 않은 곳일 경우
				elif board[ny][nx] == 0 and dist[ny][nx] == -1:
					dist[ny][nx] = dist[y][x] + 1
					queue.append([ny, nx])
	
	return int(1e9)

min_len = int(1e9)
for i in range(1, val):
	len = connect_land(i)
	if len < min_len:
		min_len = len
print(min_len)
