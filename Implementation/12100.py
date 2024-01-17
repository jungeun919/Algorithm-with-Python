import sys

input = sys.stdin.readline

n = int(input())

board = []
for _ in range(n):
	board.append(list(map(int, input().split())))

def move_up(board):
	new_board = [[0] * n for _ in range(n)]

	for c in range(n):
		fill_pos = 0
		last_val = 0
		for r in range(n):
			if board[r][c] != 0:
				if last_val == 0:
					last_val = board[r][c]
				elif last_val == board[r][c]:
					new_board[fill_pos][c] = 2 * last_val
					last_val = 0
					fill_pos += 1
				elif last_val != board[r][c]:
					new_board[fill_pos][c] = last_val
					last_val = board[r][c]
					fill_pos += 1
		
		if last_val != 0:
			new_board[fill_pos][c] = last_val
	
	return new_board

def move_down(board):
	new_board = [[0] * n for _ in range(n)]

	for c in range(n):
		fill_pos = n - 1
		last_val = 0
		for r in range(n-1, -1, -1):
			if board[r][c] != 0:
				if last_val == 0:
					last_val = board[r][c]
				elif last_val == board[r][c]:
					new_board[fill_pos][c] = 2 * last_val
					last_val = 0
					fill_pos -= 1
				elif last_val != board[r][c]:
					new_board[fill_pos][c] = last_val
					last_val = board[r][c]
					fill_pos -= 1
		
		if last_val != 0:
			new_board[fill_pos][c] = last_val
	
	return new_board

def move_left(board):
	new_board = [[0] * n for _ in range(n)]

	for r in range(n):
		fill_pos = 0
		last_val = 0
		for c in range(n):
			if board[r][c] != 0:
				# print("r:", r, "c:", c, "->", last_val, board[r][c])
				if last_val == 0:
					last_val = board[r][c]
				elif last_val == board[r][c]:
					new_board[r][fill_pos] = 2 * last_val
					last_val = 0
					fill_pos += 1
				elif last_val != board[r][c]:
					new_board[r][fill_pos] = last_val
					last_val = board[r][c]
					fill_pos += 1
		
		if last_val != 0:
			new_board[r][fill_pos] = last_val
	
	return new_board

def move_right(board):
	new_board = [[0] * n for _ in range(n)]

	for r in range(n):
		fill_pos = n - 1
		last_val = 0
		for c in range(n-1, -1, -1):
			if board[r][c] != 0:
				if last_val == 0:
					last_val = board[r][c]
				elif last_val == board[r][c]:
					new_board[r][fill_pos] = 2 * last_val
					last_val = 0
					fill_pos -= 1
				elif last_val != board[r][c]:
					new_board[r][fill_pos] = last_val
					last_val = board[r][c]
					fill_pos -= 1
		
		if last_val != 0:
			new_board[r][fill_pos] = last_val
	
	return new_board

def move_board(board, dir):
	if dir == 0: # 상
		return move_up(board)
	elif dir == 1: # 하
		return move_down(board)
	elif dir == 2: # 좌
		return move_left(board)
	elif dir == 3: # 우
		return move_right(board)

def print_board(board):
	print("print_board")
	for i in range(n):
		print(board[i])

def dfs(board, move):
	if move == 0:
		return max(max(row) for row in board)
	
	max_tile = 0
	for i in range(4):
		new_board = move_board(board, i)
		max_tile = max(max_tile, dfs(new_board, move - 1))
	
	return max_tile

res = dfs(board, 5)

print(res)
