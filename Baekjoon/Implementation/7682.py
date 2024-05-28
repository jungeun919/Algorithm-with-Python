# 처음 놓는 사람 A (X말) / 다음에 놓는 사람 B (O말)
# 1) A가 이긴 경우 -> X개수 = O개수 + 1
# 2) B가 이긴 경우 -> X개수 = O개수
# 3) 비긴 경우 -> X개수: 5, O개수: 4 (게임판 꽉 채움)

import sys

input = sys.stdin.readline

def check_winner(board):
    winners = set()

    # 가로
    if board[0] == board[1] == board[2] != '.':
        winners.add(board[0])
    if board[3] == board[4] == board[5] != '.':
        winners.add(board[3])
    if board[6] == board[7] == board[8] != '.':
        winners.add(board[6])
    # 세로
    if board[0] == board[3] == board[6] != '.':
        winners.add(board[0])
    if board[1] == board[4] == board[7] != '.':
        winners.add(board[1])
    if board[2] == board[5] == board[8] != '.':
        winners.add(board[2])
    # 대각선
    if board[0] == board[4] == board[8] != '.':
        winners.add(board[0])
    if board[2] == board[4] == board[6] != '.':
        winners.add(board[2])

    return winners

def check_valid(board):
    x_cnt = board.count('X')
    o_cnt = board.count('O')

    if not (x_cnt == o_cnt + 1 or x_cnt == o_cnt):
        return "invalid"

    winners = check_winner(board)
    x_wins = 'X' in winners
    o_wins = 'O' in winners

    if x_wins and o_wins:
        return "invalid"

    if x_wins and x_cnt == o_cnt + 1:
        return "valid"
    elif o_wins and x_cnt == o_cnt:
        return "valid"
    elif not x_wins and not o_wins and x_cnt == 5 and o_cnt == 4:
        return "valid"
    else:
        return "invalid"

while True:
    board = input().rstrip()
    if board == "end":
        break

    print(check_valid(board))
