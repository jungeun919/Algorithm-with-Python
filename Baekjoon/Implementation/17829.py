import sys

input = sys.stdin.readline

N = int(input())

board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

def get_second_num(board, r, c):
    nums = [board[r][c], board[r+1][c], board[r][c+1], board[r+1][c+1]]
    nums.sort()
    return nums[-2]

def pooling(board):
    size = len(board) // 2
    new_board = [[None] * size for _ in range(size)]

    for i in range(size):
        for j in range(size):
            new_board[i][j] = get_second_num(board, 2*i, 2*j)
    return new_board

while len(board) != 1:
    board = pooling(board)
print(board[0][0])
