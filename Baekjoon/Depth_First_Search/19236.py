import sys
import copy

input = sys.stdin.readline

board = [[None] * 4 for _ in range(4)]

for i in range(4):
    info = list(map(int, input().split()))
    for j in range(4):
        fish = j*2 # 물고기 번호
        d = j*2+1 # 방향
        board[i][j] = [info[fish], info[d]-1]

def print_board():
    for row in board:
        print(" ".join(map(str, row)))
    print()

dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, -1, -1, -1, 0, 1, 1, 1]

def get_fish_pos(fish_num, board):
    for r in range(4):
        for c in range(4):
            if board[r][c][0] == fish_num:
                return [r, c]
    return None

def move_all_fish(r_shark, c_shark, board):
    for fish_num in range(1, 17):
        pos = get_fish_pos(fish_num, board)
        if pos:
            r_fish, c_fish = pos
            d = board[r_fish][c_fish][1]

            for _ in range(8): # 45도씩 반시계 방향으로 회전
                nr_fish = r_fish + dr[d]
                nc_fish = c_fish + dc[d]

                if 0 <= nr_fish < 4 and 0 <= nc_fish < 4 and not (nr_fish == r_shark and nc_fish == c_shark):
                    board[r_fish][c_fish][1] = d
                    board[r_fish][c_fish], board[nr_fish][nc_fish] = board[nr_fish][nc_fish], board[r_fish][c_fish]
                    break

                d = (d+1) % 8

def dfs(r_shark, c_shark, eat_count, board):
    global max_eat

    cp_board = copy.deepcopy(board)
    eat_count += cp_board[r_shark][c_shark][0]
    max_eat = max(max_eat, eat_count)
    cp_board[r_shark][c_shark][0] = None

    # 물고기 이동
    move_all_fish(r_shark, c_shark, cp_board)

    # 상어 이동
    d = cp_board[r_shark][c_shark][1] # 이동 방향
    for i in range(1, 4): # 최대 3칸 이동 가능 (4*4)
        # 한 방향으로만 이동
        nr_shark = r_shark + dr[d] * i
        nc_shark = c_shark + dc[d] * i
        if 0 <= nr_shark < 4 and 0 <= nc_shark < 4:
            if cp_board[nr_shark][nc_shark][0] != None:
                dfs(nr_shark, nc_shark, eat_count, cp_board)

max_eat = 0
dfs(0, 0, 0, board)
print(max_eat)
