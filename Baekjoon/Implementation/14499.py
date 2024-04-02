import sys

input = sys.stdin.readline

n, m, x, y, k = map(int, input().split())

board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

dir = list(map(int, input().split()))

#       위 뒤  우 왼  앞 아래
dice = [0, 0, 0, 0, 0, 0]

def turn(d, dice):
    if d == 1: # 동
       return [dice[3], dice[1], dice[0], dice[5], dice[4], dice[2]]
    elif d == 2: # 서
        return [dice[2], dice[1], dice[5], dice[0], dice[4], dice[3]]
    elif d == 3: # 남
        return [dice[4], dice[0], dice[2], dice[3], dice[5], dice[1]]
    elif d == 4: # 북
        return [dice[1], dice[5], dice[2], dice[3], dice[0], dice[4]]

#        동  서  남  북
dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]

for d in dir:
    nx = x + dx[d]
    ny = y + dy[d]
    if not(0 <= nx < n and 0 <= ny < m):
        continue
    dice = turn(d, dice)
    if board[nx][ny] == 0:
        board[nx][ny] = dice[-1]
    else:
        dice[-1] = board[nx][ny]
        board[nx][ny] = 0

    print(dice[0])
    x, y = nx, ny
