from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

board = []
for _ in range(n):
	board.append(list(map(int, input().rstrip())))

# dist[y][x][0]: 벽을 부수지 않은 상태에서의 최단 거리
# dist[y][x][1]: 벽을 부순 상태에서의 최단 거리
dist = [[[0] * 2 for _ in range(m)] for _ in range(n)]

def bfs():
	#     상  하  좌  우
	dx = [0, 0, -1, 1]
	dy = [1, -1, 0, 0]

	queue = deque()
	queue.append([0, 0, 0]) # [y, x, 벽 부순 여부]
	dist[0][0][0] = 1

	while queue:
		y, x, wall = queue.popleft()

		if y == n - 1 and x == m - 1:
			return dist[y][x][wall]
				
		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]
			
			if 0 <= ny < n and 0 <= nx < m:
				# 이동할 수 없고, 벽을 부순 적이 없는 경우
				if board[ny][nx] == 1 and wall == 0:
					dist[ny][nx][1] = dist[y][x][0] + 1
					queue.append([ny, nx, 1])
				# 이동할 수 있고, 아직 방문하지 않은 경우
				elif board[ny][nx] == 0 and dist[ny][nx][wall] == 0:
					dist[ny][nx][wall] = dist[y][x][wall] + 1
					queue.append([ny, nx, wall])
	
	return -1

res = bfs()

print(res)
