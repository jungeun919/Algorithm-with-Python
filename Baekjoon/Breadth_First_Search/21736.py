from collections import deque
import sys

input = sys.stdin.readline

N, M = map(int, input().split())

board = []
for i in range(N):
	board.append(input().rstrip())
	for j in range(M):
		if board[i][j] == 'I':
			start_r, start_c = i, j

#     상  하  좌  우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(start_r, start_c):
	visited = [[False] * M for _ in range(N)]
	count = 0

	queue = deque()
	queue.append([start_r, start_c])
	visited[start_r][start_c] = True

	while queue:
		r, c = queue.popleft()

		for d in range(4):
			nr = r + dr[d]
			nc = c + dc[d]
			if 0 <= nr < N  and 0 <= nc < M:
				if visited[nr][nc] == False:
					if board[nr][nc] != 'X':
						if board[nr][nc] == 'P':
							count += 1
						queue.append([nr, nc])
						visited[nr][nc] = True
		
	return count

count = bfs(start_r, start_c)

if count == 0:
	print("TT")
else:
	print(count)
