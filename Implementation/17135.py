from collections import deque
from copy import deepcopy
import sys

input = sys.stdin.readline

n, m, d = map(int, input().split())

board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

castle = [i for i in range(m)]

#     좌  상  우
dx = [-1, 0, 1]
dy = [0, -1, 0]

# 궁수 조합
soldier_comb = []
def get_comb(arr, start):
    if len(arr) == 3:
        soldier_comb.append(arr[:])
        return

    if len(arr) > 3:
        return

    for idx in range(start, len(castle)):
        if castle[idx] not in arr:
            arr.append(castle[idx])
            get_comb(arr, idx + 1)
            arr.pop()

get_comb([], 0)

def target_enemy(row, col):
    queue = deque()
    queue.append([row-1, col, 1])

    while queue:
        y, x, dist = queue.popleft()

        if dist > d:
            return ()

        if cp_board[y][x] == 1:
            return (y, x)

        for i in range(3):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= ny < n and 0 <= nx < m:
                queue.append([ny, nx, dist+1])

def arrive_enemy():
    count = 0
    for i in range(m):
        if cp_board[n-1][i] == 1:
            count += 1
    return count

def move_enemy():
    for r in range(n-1, 0, -1):
        for c in range(m):
            cp_board[r][c] = cp_board[r-1][c]

    for i in range(m):
        cp_board[0][i] = 0

# 초기 적 수 계산
init_enemy_count = 0
for r in range(n):
    for c in range(m):
        if board[r][c] == 1:
            init_enemy_count += 1

max_rm_count = 0
for comb in soldier_comb:
    cp_board = deepcopy(board)
    enemy_count = init_enemy_count
    rm_count = 0

    while enemy_count > 0:
        attack = set()
        for solider in comb:
            attack_pos = target_enemy(n, solider)
            if attack_pos:
                attack.add(attack_pos)

        for y, x in attack:
            cp_board[y][x] = 0

        rm_count += len(attack)
        enemy_count -= len(attack) # 공격받은 적 제외
        enemy_count -= arrive_enemy() # 성에 도착할 적 제외

        move_enemy()

    max_rm_count = max(max_rm_count, rm_count)
print(max_rm_count)
