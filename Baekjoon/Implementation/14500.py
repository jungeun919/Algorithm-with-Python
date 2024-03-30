import sys

input = sys.stdin.readline

n, m = map(int, input().split())

board = []
for _ in range(n):
	board.append(list(map(int, input().split())))

visited = [[False] * m for _ in range(n)]

#     상  하  좌  우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

# ㅗ ㅜ ㅓ ㅏ 제외한 테트로미노
def dfs(y, x, val, count):
	global max_val

	if count == 4:
		max_val = max(max_val, val)
		return
	
	for i in range(4):
		ny = y + dy[i]
		nx = x + dx[i]

		if 0 <= ny < n and 0 <= nx < m:
			if visited[ny][nx] == False:
				visited[ny][nx] = True
				dfs(ny, nx, val + board[ny][nx], count + 1)
				visited[ny][nx] = False

# ㅗ ㅜ ㅓ ㅏ 모양 테트로미노
def exclude_one(y, x):
	global max_val

	for i in range(4):
		val = board[y][x]
		for j in range(3):
			d = (n + j) % 4
			ny = y + dy[d]
			nx = y + dy[d]

			if not(0 <= ny < n and 0 <= nx < m):
				val = 0
				break
			else:
				val += board[ny][nx]
		max_val = max(max_val, val)

max_val= 0

for row in range(n):
	for col in range(m):
		visited[row][col] = True
		dfs(row, col, board[row][col], 1)
		visited[row][col] = False

		exclude_one(row, col)

print(max_val)
