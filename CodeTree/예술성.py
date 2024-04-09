from collections import deque

n = int(input())

board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

#     상  하  좌  우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(r, c, val, group_idx):
    queue = deque()
    queue.append([r, c])
    visited[r][c] = True
    group[r][c] = group_idx
    group_count[group_idx] += 1

    while queue:
        r, c = queue.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < n and 0 <= nc < n and \
                visited[nr][nc] == False and board[nr][nc] == val:
                queue.append([nr, nc])
                visited[nr][nc] = True
                group[nr][nc] = group_idx
                group_count[group_idx] += 1

def make_group():
    group_idx = 0 # 그룹별 인덱스, 그룹 개수

    for r in range(n):
        for c in range(n):
            if visited[r][c] == False:
                bfs(r, c, board[r][c], group_idx)
                group_idx += 1
    
def get_score():
    score = 0
    for r in range(n):
        for c in range(n):
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                # 다른 그룹일 경우
                if 0 <= nr < n and 0 <= nc < n and group[r][c] != group[nr][nc]:
                    idx_a, idx_b = group[r][c], group[nr][nc]
                    count_group_a, count_group_b = group_count[idx_a], group_count[idx_b]
                    group_a_num, group_b_num = board[r][c], board[nr][nc]
                    
                    score += (count_group_a + count_group_b) * group_a_num * group_b_num
    return score // 2

# n = 5 (반시계 방향으로 90도 회전)
#           (0,2)                          (2,4)
#           (1,2)                          (2,3)
# (2,0)(2,1)(2,2)(2,3)(2,4)      (0,2)(1,2)(2,2)(3,2)(4,2)
#           (3,2)                          (2,1)
#           (4,2)                          (2,0)

def rotate_plus():
    for r in range(n):
        for c in range(n):
            if c == n//2: # 세로줄 (r,c) -> (c,r)
                temp_board[c][r] = board[r][c]
            elif r == n//2: # 가로줄 (r,c) -> (n-c-1,r)
                temp_board[n-c-1][r] = board[r][c]

# n == 3 (시계 방향으로 90도 회전)
# 1 2 3      7 4 1 
# 4 5 6      8 5 2
# 7 8 9      9 6 3

# (0,0)(0,1)(0,2)  (2,0)(1,0)(0,0)
# (1,0)(1,1)(1,2)  (2,1)(0,1)(0,1)
# (2,0)(2,1)(2,2)  (2,2)(1,2)(0,2)

def rotate_square(start_r, start_c, size):
    for r in range(size):
        for c in range(size):
            temp_board[start_r + r][start_c + c] = board[start_r + size-c-1][start_c + r]

total_score = 0
for _ in range(4): # 초기, 1~3 예술 점수 구하기
    # make group
    visited = [[False] * n for _ in range(n)]

    group = [[-1] * n for _ in range(n)] # 같은 그룹끼리 같은 인덱스
    group_count = [0] * n * n # 그룹 인덱스로 접근 -> 요소 개수
    
    make_group()
    total_score += get_score()

    # rotate board
    temp_board = [row[:] for row in board]

    rotate_plus()
    rotate_square(0, 0, n//2)
    rotate_square(0, n//2+1, n//2)
    rotate_square(n//2+1, 0, n//2)
    rotate_square(n//2+1, n//2+1, n//2)

    board = temp_board

print(total_score)
