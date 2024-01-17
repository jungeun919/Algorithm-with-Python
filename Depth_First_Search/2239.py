import sys

input = sys.stdin.readline

board = []
blank = []

for _ in range(9):
    board.append(list(map(int, input().rstrip())))

for y in range(9):
    for x in range(9):
        if board[y][x] == 0:
            blank.append((y, x))

def check_row(y, val):
    for i in range(9):
        if board[y][i] == val:
            return False
    return True

def check_col(x, val):
    for i in range(9):
        if board[i][x] == val:
            return False
    return True

def check_rect(y, x, val):
    start_row = y // 3 * 3
    start_col = x // 3 * 3
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == val:
                return False
    return True

def dfs(idx):
    if idx == len(blank):
        for i in range(9):
            print(*board[i], sep="")
        exit(0)
    
    y = blank[idx][0]
    x = blank[idx][1]
    for i in range(1, 10): # 채울 값
        if check_row(y, i) and check_col(x, i) and check_rect(y, x, i):
            board[y][x] = i
            dfs(idx + 1) # 다음 blank 채우기
            board[y][x] = 0

dfs(0)
