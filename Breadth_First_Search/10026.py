from collections import deque
import sys

input = sys.stdin.readline

n = int(input())

graph = []
for _ in range(n):
	graph.append(list(input().rstrip()))

#     상  하  좌  우
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def bfs(row, col, visited):
	queue = deque()
	queue.append([row, col])
	visited[row][col] = True
	color = graph[row][col]

	while queue:
		y, x = queue.popleft()

		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]

			if 0 <= nx < n and 0 <= ny < n:
				if visited[ny][nx] == False and graph[ny][nx] == color:
					queue.append([ny, nx])
					visited[ny][nx] = True

normal_area = 0
visited = [[False] * n for _ in range(n)]

for row in range(n):
	for col in range(n):
		if visited[row][col] == False:
			bfs(row, col, visited)
			normal_area += 1

blind_area = 0
visited = [[False] * n for _ in range(n)]

# R -> G
for row in range(n):
	for col in range(n):
		if graph[row][col] == 'R':
			graph[row][col] = 'G'

for row in range(n):
	for col in range(n):
		if visited[row][col] == False:
			bfs(row, col, visited)
			blind_area += 1

print(normal_area, blind_area)
