from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

graph = []
for _ in range(n):
	graph.append(list(map(int, input().split())))

def print_array(array):
	for i in range(n):
		print(' '.join(map(str, array[i])))

#     상  하  좌  우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(y, x):
	queue = deque()
	queue.append([y, x])
	visited[y][x] = True

	while queue:
		y, x = queue.popleft()

		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]

			if 0 <= ny < n and 0 <= nx < m and visited[ny][nx] == False:
				if graph[ny][nx] != 0:
					queue.append([ny, nx])
					visited[ny][nx] = True
				else:
					graph[y][x] -= 1
					if graph[y][x] < 0:
						graph[y][x] = 0

time = 0

while True:
	iceberg = 0
	visited = [[False] * m for _ in range(n)]

	for r in range(n):
		for c in range(m):
			if graph[r][c] != 0 and visited[r][c] == False:
				bfs(r, c)
				iceberg += 1
	
	if iceberg == 0:
		time = 0
		break
	if iceberg >= 2:
		break

	time += 1

print(time)
