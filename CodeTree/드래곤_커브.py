n = int(input())

#     동  북  서  남
dx = [0, -1, 0, 1] # row
dy = [1, 0, -1, 0] # col

visited = [[False] * 101 for _ in range(101)]

for _ in range(n):
    x, y, d, g = map(int, input().split()) # r, c, d, g
    visited[x][y] = True

    curve = [d]
    for _ in range(g):
        for i in range(len(curve)-1, -1, -1):
            next_d = (curve[i] + 1) % 4
            curve.append(next_d)
    
    for d in curve:
        x += dx[d]
        y += dy[d]

        if 0 <= x <= 100 and 0 <= y <= 100:
            visited[x][y] = True

count = 0
for r in range(100):
    for c in range(100):
        if visited[r][c] == True and visited[r][c+1] == True and \
            visited[r+1][c] == True and visited[r+1][c+1] == True:
            count += 1
print(count)
