# 3개 빙고 최소 조건 -> 12개 확인
# x x o x o
# x x o o x
# x x o x x
# o o o o o
# o x o x x

import sys

input = sys.stdin.readline

board = []
for _ in range(5):
    board.append(list(map(int, input().split())))

call = []
for _ in range(5):
    call += list(map(int, input().split()))

def check(board):
    bingo = 0

    # 가로
    for i in range(5):
        if board[i].count(0) == 5:
            bingo += 1

    # 세로
    for c in range(5):
        count = 0
        for r in range(5):
            if board[r][c] == 0:
                count += 1
        if count == 5:
            bingo += 1

    # 대각선 \
    count = 0
    for i in range(5):
        if board[i][i] == 0:
            count += 1
    if count == 5:
        bingo += 1

    # 대각선 /
    count = 0
    for i in range(5):
        if board[i][4-i] == 0:
            count += 1
    if count == 5:
        bingo += 1

    return bingo

count = 0 # 지운 개수
for i in range(25):
    for r in range(5):
        for c in range(5):
            if board[r][c] == call[i]:
                board[r][c] = 0
                count += 1

    if count >= 12:
        bingo = check(board)
        if bingo >= 3:
            print(i+1)
            break
