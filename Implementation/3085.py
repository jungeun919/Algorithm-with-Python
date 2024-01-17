# import sys

# input = sys.stdin.readline

# n = int(input())

# board = []
# for _ in range(n):
# 	board.append(list(input().rstrip()))

# max_count = 0

# def check_count(board):
# 	max_count = 1

# 	for i in range(n):
# 		# row 조회
# 		count = 1
# 		for j in range(n-1):
# 			if board[j][i] == board[j+1][i]:
# 				count += 1
# 			else:
# 				count = 1
# 			max_count = max(max_count, count)
		
# 		# col 조회
# 		count = 1
# 		for j in range(n-1):
# 			if board[i][j] == board[i][j+1]:
# 				count += 1
# 			else:
# 				count = 1
# 			max_count = max(max_count, count)
	
# 	return max_count


# for row in range(n):
# 	for col in range(n):
# 		# 행 범위 검사
# 		if row + 1 < n:
# 			board[row][col], board[row+1][col] = board[row+1][col], board[row][col]
# 			max_count = max(max_count, check_count(board))
# 			board[row][col], board[row+1][col] = board[row+1][col], board[row][col]
		
# 		# 열 범위 검사
# 		if col + 1 < n:
# 			board[row][col], board[row][col+1] = board[row][col+1], board[row][col]
# 			max_count = max(max_count, check_count(board))
# 			board[row][col], board[row][col+1] = board[row][col+1], board[row][col]

# print(max_count)


import sys

input = sys.stdin.readline

n = int(input())

board = []
for _ in range(n):
	board.append(list(input().rstrip()))

max_count = 0

def check_count(board):
	max_count = 1

	for i in range(n):
		# row 조회
		count = 1
		for j in range(n-1):
			if board[j][i] == board[j+1][i]:
				count += 1
			else:
				count = 1
			max_count = max(max_count, count)
		
		# col 조회
		count = 1
		for j in range(n-1):
			if board[i][j] == board[i][j+1]:
				count += 1
			else:
				count = 1
			max_count = max(max_count, count)
	
	return max_count


#     상  하  좌  우
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

for y in range(n):
	for x in range(n):
		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]

			if 0 <= nx < n and 0 <= ny < n:
				if board[y][x] != board[ny][nx]:
					board[y][x], board[ny][nx] = board[ny][nx], board[y][x]
					max_count = max(max_count, check_count(board))
					board[y][x], board[ny][nx] = board[ny][nx], board[y][x]

print(max_count)
