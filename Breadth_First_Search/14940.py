from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

graph = []
for _ in range(n):
	graph.append(list(map(int, input().split())))

visited = [[-1] * m for _ in range(n)]

def bfs(row, col):
	#     상  하  좌  우
	dx = [0, 0, -1, 1]
	dy = [1, -1, 0, 0]

	queue = deque()
	queue.append([row, col])
	visited[row][col] = 0

	while queue:
		y, x = queue.popleft()

		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]

			if 0 <= ny < n and 0 <= nx < m and visited[ny][nx] == -1:
				if graph[ny][nx] == 0:
					visited[ny][nx] = 0
				elif graph[ny][nx] == 1:
					visited[ny][nx] = visited[y][x] + 1
					queue.append([ny, nx])

for row in range(n):
	for col in range(m):
		if graph[row][col] == 2:
			bfs(row, col)

for row in range(n):
	for col in range(m):
		if graph[row][col] == 0:
			print(0, end=" ")
		else:
			print(visited[row][col], end=" ")
	print()
