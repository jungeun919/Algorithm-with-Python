from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

board = []
for _ in range(n):
	board.append(list(map(int, input().split())))

#     상  하  좌  우
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

# 섬 구분짓기
def labeling_land(row, col, val):
	queue = deque()
	queue.append([row, col, val])
	board[row][col] = val
	visited[row][col] = 1

	while queue:
		y, x, val = queue.popleft()

		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]

			if 0 <= nx < m and 0 <= ny < n and board[ny][nx] == 1:
				board[ny][nx] = val
				visited[row][col] = 1
				queue.append([ny, nx, val])

visited = [[0] * m for _ in range(n)]

val = 2
for row in range(n):
	for col in range(m):
		if board[row][col] == 1 and visited[row][col] == 0:
			labeling_land(row, col, val)
			val += 1

print("====================")
for row in range(n):
	for col in range(m):
		print(board[row][col], end=' ')
	print()
print("====================")

# 섬을 이어주는 다리 생성
# def make_bridge(row, col, start_land):
# 	queue = deque()

# 	# 한 방향으로만 이동
# 	for i in range(4):
# 		queue.append([row, col])
# 		visited = [[0] * m for _ in range(n)]
# 		dist = [[0] * m for _ in range(n)]
# 		visited[row][col] = 1

# 		while queue:
# 			y, x = queue.popleft()
# 			nx = x + dx[i]
# 			ny = y + dy[i]

# 			if 0 <= nx < m and 0 <= ny < n and visited[ny][nx] == 0:
# 				# 바다일 경우 다리 생성
# 				if board[ny][nx] == 0:
# 					visited[ny][nx] = 1
# 					dist[ny][nx] = dist[y][x] + 1
# 					queue.append([ny, nx])
# 				# 바다가 아니고, 다리의 시작섬이 아니고, 다리 길이가 2 이상일 경우
# 				elif board[ny][nx] != start_land and dist[y][x] >= 2:
# 					bridges.append([dist[y][x], start_land, board[ny][nx]])

def make_bridge(row, col, start_land):
	queue = deque()

	# 한 방향으로만 이동
	for i in range(4):
		queue.append([row, col])
		dist = [[-1] * m for _ in range(n)]
		dist[row][col] = 0

		while queue:
			y, x = queue.popleft()
			nx = x + dx[i]
			ny = y + dy[i]

			if 0 <= nx < m and 0 <= ny < n and dist[ny][nx] == -1:
				# 바다일 경우 다리 생성
				if board[ny][nx] == 0:
					dist[ny][nx] = dist[y][x] + 1
					queue.append([ny, nx])
				# 바다가 아니고, 다리의 시작섬이 아니고, 다리 길이가 2 이상일 경우
				elif board[ny][nx] != start_land and dist[y][x] >= 2:
					bridges.append([dist[y][x], start_land, board[ny][nx]])

bridges = []
for row in range(n):
	for col in range(m):
		if board[row][col] != 0:
			make_bridge(row, col, board[row][col])

print("[dist, start, end]")
print("bridges:", bridges)

# 크루스칼
parent = [i for i in range(val + 1)] # 자기자신을 부모로 초기화

def find_parent(node):
	if node != parent[node]:
		parent[node] = find_parent(parent[node])
	return parent[node]

def union_parent(x, y):
	x = find_parent(x)
	y = find_parent(y)

	if x > y: # 작은 쪽이 부모로
		parent[x] = y
	else:
		parent[y] = x

res = 0
land_count = 0

bridges.sort()
print("bridges:", bridges)

for dist, a, b in bridges:
	if find_parent(a) != find_parent(b):
		union_parent(a, b)
		res += dist
		land_count += 1
		if land_count == val - 2: # 모든 섬을 연결한 경우
			break

if land_count == val - 2:
	print(res)
else:
	print(-1)
