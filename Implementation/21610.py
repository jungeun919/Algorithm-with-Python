import sys

input = sys.stdin.readline

n, m = map(int, input().split())

board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

clouds = [(n-1, 0), (n-1, 1), (n-2, 0), (n-2, 1)]

for _ in range(m):
    d, s = map(int, input().split())

    moved_clouds = []
    for y, x in clouds:
        ny = (y + dy[d-1] * s) % n
        nx = (x + dx[d-1] * s) % n
        board[ny][nx] += 1
        moved_clouds.append((ny, nx))

    for y, x in moved_clouds:
        count = 0
        for d in range(1, 8, 2): # 대각선 4방향:
            ny = y + dy[d]
            nx = x + dx[d]
            if not(0 <= ny < n and 0 <= nx < n):
                continue
            if board[ny][nx] > 0:
                count += 1
        board[y][x] += count

    new_clouds = []
    for y in range(n):
        for x in range(n):
            if board[y][x] >= 2 and (y, x) not in moved_clouds:
                new_clouds.append((y, x))
                board[y][x] -= 2
    clouds = new_clouds

res = 0
for y in range(n):
    for x in range(n):
        res += board[y][x]
print(res)
