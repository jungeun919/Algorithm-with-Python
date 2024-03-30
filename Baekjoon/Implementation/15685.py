# 세대 | 선분의 개수 | 방향
# 0   | 1 (2^0)  | 0
# 1   | 2 (2^1)  | 0 1
# 2   | 4 (2^2)  | 0 1 2 1
# 3   | 8 (2^3)  | 0 1 2 1 2 3

import sys

input = sys.stdin.readline

n = int(input())

#     동  북  서  남
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

visited = [[False] * 101 for _ in range(101)]

for _ in range(n):
    x, y, d, g = map(int, input().split())
    visited[y][x] = True

    curve = [d] # 시작 방향
    for _ in range(g): # 세대
        for i in range(len(curve) -1, -1, -1):
            next_d = (curve[i] + 1) % 4
            curve.append(next_d)

    for d in curve:
        x += dx[d]
        y += dy[d]

        if 0 <= y <= 100 and 0 <= x <= 100:
            visited[y][x] = True

count = 0
for r in range(100):
    for c in range(100):
        if visited[r][c] == True and visited[r][c+1] == True and \
            visited[r+1][c] == True and visited[r+1][c+1] == True:
            count += 1
print(count)
