from collections import deque
import sys

input = sys.stdin.readline

n, m, k = map(int, input().split())

board = [[0 for _ in range(m)] for _ in range(n)]
for _ in range(k):
	row, col = map(int, input().split())
	board[row - 1][col - 1] = 1

def bfs(row, col):
	#     상  하  좌  우
	dx = [0, 0, -1, 1]
	dy = [1, -1, 0, 0]

	queue = deque()
	queue.append([row, col])
	board[row][col] = 0
	count = 1

	while queue:
		y, x = queue.popleft()

		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]

			if 0 <= nx < m and 0 <= ny < n and board[ny][nx] == 1:
				queue.append([ny, nx])
				board[ny][nx] = 0
				count += 1
	return count

max_count = 0
for row in range(n):
	for col in range(m):
		if board[row][col] == 1:
			count = bfs(row, col)
			max_count = max(max_count, count)

print(max_count)
