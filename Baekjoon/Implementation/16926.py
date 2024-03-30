from collections import deque
import sys

input = sys.stdin.readline

n, m, r = map(int, input().split())

board = []
for _ in range(n):
	board.append(list(input().split()))

res = [[0] * m for _ in range(n)]
queue = deque()
loops = min(n, m) // 2 # 껍질 개수

for start in range(loops):
	# 2차원 -> 1차원
	# 위, 오, 아래, 왼 (시계반대방향)
	queue.extend(board[start][start: m-start])
	queue.extend([row[m-start-1] for row in board[start+1 : n-start-1]])
	queue.extend(board[n-start-1][start : m-start][::-1])
	queue.extend([row[start] for row in board[start+1 : n-start-1][::-1]])

	# r번 회전
	queue.rotate(-r)

	# 1차원 -> 2차원
	# 위, 오, 아래, 왼 (시계반대방향)
	for j in range(start, m-start):
		res[start][j] = queue.popleft()
	for j in range(start+1, n-start-1):
		res[j][m-start-1] = queue.popleft()
	for j in range(m-start-1, start-1, -1):
		res[n-start-1][j] = queue.popleft()
	for j in range(n-start-1-1, start, -1):
		res[j][start] = queue.popleft()


for line in res:
	print(" ".join(line))
