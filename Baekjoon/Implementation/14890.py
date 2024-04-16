import sys

input = sys.stdin.readline

N, L = map(int, input().split())

board = []
for i in range(N):
    board.append(list(map(int, input().split())))

def check(line):
    installed = [False] * N

    for i in range(N-1):
        if line[i] == line[i+1]:
            continue

        elif abs(line[i] - line[i+1]) > 1:
            return False

        if line[i] > line[i+1]: # 왼쪽이 더 높음 -> 오른쪽 탐색
            for j in range(L):
                if not(0 <= i+1+j < N):
                    return False
                if line[i+1] != line[i+1+j]:
                    return False
                if installed[i+1+j] == True:
                    return False
                installed[i+1+j] = True

        else: # 오른쪽이 더 높음 -> 왼쪽 탐색
            for j in range(L):
                if not(0 <= i-j < N):
                    return False
                if line[i] != line[i-j]:
                    return False
                if installed[i-j] == True:
                    return False
                installed[i-j] = True

    return True

count = 0

for row in board:
    if check(row):
        count += 1

for j in range(N):
    line = [board[i][j] for i in range(N)]
    if check(line):
        count += 1

print(count)
