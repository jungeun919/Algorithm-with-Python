from collections import deque
import sys

input = sys.stdin.readline

r, c = map(int, input().split())

board = []
for _ in range(r):
	board.append(list(map(int, input().split())))

#     상  하  좌  우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs():
	queue = deque() # 공기
	queue.append([0, 0])
	visited[0][0] = True

	melt_count = 0 # 녹아야 될 부분

	while queue:
		y, x = queue.popleft()

		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]

			if 0 <= ny < r and 0 <= nx < c and visited[ny][nx] == False:
				visited[ny][nx] = True

				if board[ny][nx] == 0:
					queue.append([ny, nx])
				elif board[ny][nx] == 1:
					board[ny][nx] = 0
					melt_count += 1
	
	return melt_count

# 초기 치즈 개수 계산
cheese_count = 0
for y in range(r):
	for x in range(c):
		if board[y][x] == 1:
			cheese_count += 1

time = 0
while True:
	visited = [[False] * c for _ in range(r)]

	melt_count = bfs()
	time += 1
	cheese_count -= melt_count
	if cheese_count == 0: # cheese_count == melt_count
		print(time)
		print(melt_count)
		break
