import sys

input = sys.stdin.readline

r, c, t = map(int, input().split())

board = []
for _ in range(r):
	board.append(list(map(int, input().split())))

# 공기청정기 위치 구하기
for i in range(r):
	if board[i][0] == -1:
		cleaner_top = i
		cleaner_down = i + 1
		break

def dust_spread():
	# 90씩 회전한 반시계 방향
	#     동  북  서  남
	dx = [-1, 0, 1, 0]
	dy = [0, -1, 0, 1]

	dust = [[0] * c for _ in range(r)]

	for y in range(r):
		for x in range(c):
			if board[y][x] > 0:
				spread_amount = 0

				# 네 방향으로 확산
				for i in range(4):
					nx = x + dx[i]
					ny = y + dy[i]

					if 0 <= ny < r and 0 <= nx < c:
						if board[ny][nx] != -1:
							dust[ny][nx] += board[y][x] // 5
							spread_amount += board[y][x] // 5
				
				board[y][x] -= spread_amount
	
	for y in range(r):
		for x in range(c):
			board[y][x] += dust[y][x]

def top_rotate():
	# 90씩 회전한 반시계 방향
	#     동  북  서  남
	dx = [1, 0, -1, 0]
	dy = [0, -1, 0, 1]

	dir = 0
	prev = 0
	y, x = cleaner_top, 1

	while True:
		if y == cleaner_top and x == 0:
			break

		nx = x + dx[dir]
		ny = y + dy[dir]

		if not(0 <= ny < r and 0 <= nx < c):
			dir += 1
			continue
		
		board[y][x], prev = prev, board[y][x]
		y, x = ny, nx

def down_rotate():
	# 90씩 회전한 시계 방향
	#     동  남  서  북
	dx = [1, 0, -1, 0]
	dy = [0, 1, 0, -1]

	dir = 0
	prev = 0
	y, x = cleaner_down, 1

	while True:
		if y == cleaner_down and x == 0:
			break

		nx = x + dx[dir]
		ny = y + dy[dir]

		if not(0 <= ny < r and 0 <= nx < c):
			dir += 1
			continue

		board[y][x], prev = prev, board[y][x]
		y, x = ny, nx

for _ in range(t):
	dust_spread()
	print('\n----spread----')
	for row in range(r):
		print(' '.join(map(str, board[row])))
	top_rotate()
	print('\n----top rotate----')
	for row in range(r):
		print(' '.join(map(str, board[row])))
	down_rotate()
	print('\n-----down rotate----')
	for row in range(r):
		print(' '.join(map(str, board[row])))

amount = 0
for i in range(r):
	for j in range(c):
		if board[i][j] > 0: # 공기청정기 값 제외
			amount += board[i][j]
print(amount)
