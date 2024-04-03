import sys

input = sys.stdin.readline

n, m, k = map(int, input().split())

balls = []
for _ in range(m):
    r, c, m, s, d = map(int, input().split())
    balls.append([r-1, c-1, m, s, d])

board = [[[] for _ in range(n)] for _ in range(n)]

dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]

def move_balls():
    for _ in range(len(balls)):
        r, c, m, s, d = balls.pop(0)
        nr = (r + dr[d] * s) % n
        nc = (c + dc[d] * s) % n
        board[nr][nc].append([m, s, d])

def update_balls():
    for r in range(n):
        for c in range(n):
            if len(board[r][c]) == 1:
                m, s, d = board[r][c].pop(0)
                balls.append([r, c, m, s, d])

            elif len(board[r][c]) > 1:
                total_m, total_s, d_udlr, d_cross, count = 0, 0, False, False, len(board[r][c])
                for i in range(count):
                    # 같은 칸에 있는 볼 m, s, d 계산
                    m, s, d = board[r][c].pop(0)
                    total_m += m
                    total_s += s
                    if d % 2 == 0:
                        d_udlr = True
                    else:
                        d_cross = True

                # 볼 나누기
                if total_m // 5 > 0:
                    if d_udlr == True and d_cross == True:
                        # 대각선 네 방향의 값
                        for i in range(1, 8, 2):
                            balls.append([r, c, total_m // 5, total_s // count, i])
                    else:
                        # 상하좌우 방향의 값
                        for i in range(0, 8, 2):
                            balls.append([r, c, total_m // 5, total_s // count, i])

for _ in range(k):
    move_balls()
    update_balls()

total_m = 0
for ball in balls:
    total_m += ball[2]
print(total_m)
