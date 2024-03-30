from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

map = []
for _ in range(n):
	map.append(list(input().rstrip()))

def bfs(row, col):
	#     상  하  좌  우
	dx = [0, 0, -1, 1]
	dy = [1, -1, 0, 0]

	visited = [[0] * m for _ in range(n)]

	queue = deque()
	queue.append([row, col])
	visited[row][col] = 1
	time = 0

	while queue:
		y, x = queue.popleft()

		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]

			if 0 <= nx < m and 0 <= ny < n and \
				map[ny][nx] == 'L' and visited[ny][nx] == 0:
				queue.append([ny, nx])
				visited[ny][nx] = visited[y][x] + 1
				time = max(time, visited[ny][nx])
	return time - 1


time = 0
for row in range(n):
	for col in range(m):
		if map[row][col] == 'L':
			time = max(time, bfs(row, col))
print(time)
