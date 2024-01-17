from collections import deque
import sys

input = sys.stdin.readline

n, l, r = map(int, input().split())

people = []
for _ in range(n):
	people.append(list(map(int, input().split())))

#     상  하  좌  우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(a, b):
	queue = deque()
	queue.append([a, b])

	union = []
	union.append([a, b])

	visited[a][b] = True

	while queue:
		x, y = queue.popleft()

		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]

			if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == False:
				if l <= abs(people[nx][ny] - people[x][y]) <= r:
					visited[nx][ny] = True
					queue.append([nx, ny])
					union.append([nx, ny])
	return union

day = 0

while True:
	visited = [[False] * n for _ in range(n)]
	open = False # 연합이 이루어졌는지 여부 확인

	for i in range(n):
		for j in range(n):
			if visited[i][j] == 0:
				unions = bfs(i, j)

				if len(unions) > 1:
					open = True
					adjust_people = sum([people[a][b] for a, b in unions]) // len(unions)

					for a, b in unions:
						people[a][b] = adjust_people
	
	if open == False:
		break

	day += 1

print(day)
