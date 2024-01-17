from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
r1, c1, r2, c2 = map(int, input().split())

graph = [[-1] * n for _ in range(n)]

def bfs(row, col):
	move = [(-2, -1), (-2, 1), (0, -2), (0, 2), (2, -1), (2, 1)]

	queue = deque()
	queue.append([row, col])
	graph[row][col] = 0

	while queue:
		y, x = queue.popleft()

		for dy, dx in move:
			ny = y + dy
			nx = x + dx

			if 0 <= ny < n and 0 <= nx < n and graph[ny][nx] == -1:
				graph[ny][nx] = graph[y][x] + 1
				queue.append([ny, nx])

bfs(r1, c1)
print(graph[r2][c2])
