len = int(input())
path = list(input())

#     북  동  남  서
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

cur_r, cur_c = 0, 0 # 시작 위치를 (0, 0)로 가정
cur_d = 2
route_r = [0] # r 방문 좌표
route_c = [0] # c 방문 좌표

for c in path:
    if c == 'L':
        cur_d = (cur_d - 1) % 4
    elif c == 'R':
        cur_d = (cur_d + 1) % 4
    elif c == 'F':
        cur_r += dr[cur_d]
        cur_c += dc[cur_d]
        route_r.append(cur_r)
        route_c.append(cur_c)

# for r, c in zip(route_r, route_c):
#     print(r, c)

R = max(route_r) - min(route_r) + 1
C = max(route_c) - min(route_c) + 1
maze = [['#'] * C for _ in range(R)]

start_r = abs(min(route_r))
start_c = abs(min(route_c))
for r, c in zip(route_r, route_c):
    maze[r + start_r][c + start_c] = '.'

for row in maze:
    print("".join(row))
