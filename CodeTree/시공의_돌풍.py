n, m, t = map(int, input().split())

board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

# 바람 위치 구하기
for i in range(n):
    if board[i][0] == -1:
        wind_top = i
        wind_bottom = i+1
        break

def dust_spread():
    #     동  북  서  남 (반시계)
    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]

    dust = [[0] * m for _ in range(n)]

    for y in range(n):
        for x in range(m):
            if board[y][x] > 0:
                spread_amount = 0

                # 네 방향으로 확산
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= ny < n and 0 <= nx < m:
                        if board[ny][nx] != -1:
                            dust[ny][nx] += board[y][x] // 5
                            spread_amount += board[y][x] // 5
                
                board[y][x] -= spread_amount
    
    for y in range(n):
        for x in range(m):
            board[y][x] += dust[y][x]

def top_clean():
    #     동  북  서  남 (반시계)
    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]

    direction = 0
    prev = 0
    y, x = wind_top, 1

    while True:
        if y == wind_top and x == 0:
            break
        
        nx = x + dx[direction]
        ny = y + dy[direction]

        if not(0 <= ny < n and 0 <= nx < m):
            direction += 1
            continue
        
        board[y][x], prev = prev, board[y][x]
        y, x = ny, nx

def down_clean():
    #     동  남  서  북 (시계)
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    direction = 0
    prev = 0
    y, x = wind_bottom, 1

    while True:
        if y == wind_bottom and x == 0:
            break
        
        nx = x + dx[direction]
        ny = y + dy[direction]

        if not(0 <= ny < n and 0 <= nx < m):
            direction += 1
            continue
        
        board[y][x], prev = prev, board[y][x]
        y, x = ny, nx

for _ in range(t):
    dust_spread()
    top_clean()
    down_clean()

amount = 0
for r in range(n):
    for c in range(m):
        if board[r][c] > 0: # 공기청정기(-1) 제외
            amount += board[r][c]
print(amount)
