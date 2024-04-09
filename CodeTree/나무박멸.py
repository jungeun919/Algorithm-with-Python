n, m, k, c = map(int, input().split())

board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

#     상  하  좌  우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def tree_growth():
    growth = []

    for y in range(n):
        for x in range(n):
            if board[y][x] > 0:
                count = 0
                for i in range(4):
                    ny = y + dy[i]
                    nx = x + dx[i]
                    if 0 <= ny < n and 0 <= nx < n and board[ny][nx] > 0:
                        count += 1
                growth.append([y, x, count])
    
    for y, x, count in growth:
        board[y][x] += count
    
    return growth

def tree_spread(growth):
    spread = []
    for y, x, _ in growth:
        count = 0
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < n and 0 <= nx < n and \
                board[ny][nx] == 0 and weed_killer[ny][nx] == 0:
                count += 1
        
        if count > 0:
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if 0 <= ny < n and 0 <= nx < n and \
                    board[ny][nx] == 0 and weed_killer[ny][nx] == 0:
                    spread.append([ny, nx, board[y][x] // count])
    
    for y, x, count in spread:
        board[y][x] += count

# 대각선 상좌 상우 하좌 하우
diagonal_dx = [-1, 1, -1, 1]
diagonal_dy = [-1, -1, 1, 1]

def weed_killer_reduce():
    for y in range(n):
        for x in range(n):
            if weed_killer[y][x] > 0:
                weed_killer[y][x] -= 1

def find_max_kill_place():
    place = []

    for y in range(n):
        for x in range(n):
            count = 0
            if board[y][x] > 0:
                count += board[y][x]
                for i in range(4): # 대각선 방향
                    cur_y, cur_x = y, x
                    for _ in range(k): # k칸 만큼 전파
                        next_y = cur_y + diagonal_dy[i]
                        next_x = cur_x + diagonal_dx[i]

                        if not(0 <= next_y < n and 0 <= next_x < n):
                            break
                        
                        if board[next_y][next_x] <= 0: # 나무가 없을 경우
                            break
                        
                        count += board[next_y][next_x]
                        cur_y, cur_x = next_y, next_x
            
            place.append([y, x, count])
    
    place.sort(key=lambda x: (-x[2], x[0], x[1]))

    return place[0]

def tree_kill(y, x):
    weed_killer[y][x] = c # c년 동안 제초제 유지
    board[y][x] = 0

    for i in range(4): # 대각선 방향
        cur_y, cur_x = y, x
        for _ in range(k): # k칸 만큼 전파
            next_y = cur_y + diagonal_dy[i]
            next_x = cur_x + diagonal_dx[i]

            if not(0 <= next_y < n and 0 <= next_x < n):
                break
            
            if board[next_y][next_x] == -1: # 벽일 경우
                break
            
            if board[next_y][next_x] == 0: # 빈 칸일 경우
                weed_killer[next_y][next_x] = c
                break
            
            weed_killer[next_y][next_x] = c
            board[next_y][next_x] = 0
            cur_y, cur_x = next_y, next_x

weed_killer = [[0] * n for _ in range(n)] # 제초제가 유지되는 기간
res = 0

for _ in range(m):
    # 나무의 성장
    growth = tree_growth()

    # 나무의 번식
    tree_spread(growth)

    # 제초제 시간 감소
    weed_killer_reduce()

    # 제초제를 뿌릴 위치 선정
    y, x, count = find_max_kill_place()

    # 칸에 제초제를 뿌리는 작업 진행
    if board[y][x] > 0:
        tree_kill(y, x)
    res += count

print(res)
