from collections import deque
import sys

input = sys.stdin.readline

row, col, k = map(int, input().split())

graph = [[0] * col for _ in range(row)]

for _ in range(k):
	x1, y1, x2, y2 = map(int, input().split())
	for r in range(y1, y2):
		for c in range(x1, x2):
			graph[r][c] += 1

#     상  하  좌  우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(r, c):
	queue = deque()
	queue.append([r, c])
	graph[r][c] = 1
	area = 1

	while queue:
		y, x = queue.popleft()

		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]

			if 0 <= ny < row and 0 <= nx < col and graph[ny][nx] == 0:
				graph[ny][nx] = 1
				queue.append([ny, nx])
				area += 1
	return area

area = []
for r in range(row):
	for c in range(col):
		if graph[r][c] == 0:
			area.append(bfs(r, c))

area.sort()

print(len(area))
for i in area:
	print(i, end=" ")
