from collections import Counter
import sys

input = sys.stdin.readline

r, c, k = map(int, input().split())

board = []
for _ in range(3):
    board.append(list(map(int, input().split())))

def sort_board(board):
    sorted_board = []
    max_len = 0

    for row in board:
        sorted_row = []
        counter = Counter(row) # Counter({2: 1, 1: 1, 3: 1})
        for key, value in sorted(counter.items(), key=lambda x: (x[1], x[0])): # 등장 횟수, 숫자 오름차순
            if key == 0:
                continue
            sorted_row.extend([key, value])
        max_len = max(max_len, len(sorted_row))
        sorted_board.append(sorted_row)

    for row in sorted_board:
        row.extend([0] * (max_len - len(row)))

    return sorted_board

time = 0
while True:
    if time > 100:
        time = -1
        break

    if r-1 < len(board) and c-1 < len(board[0]):
        if board[r-1][c-1] == k:
            break

    if len(board) >= len(board[0]): # 행 >= 열
        board = sort_board(board)
    else:
        board = list(map(list, zip(*board))) # transpose
        board = sort_board(board)
        board = list(map(list, zip(*board))) # 다시 transpose

    time += 1
print(time)
