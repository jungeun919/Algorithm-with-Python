import sys

input = sys.stdin.readline

A, B = map(int, input().split()) # 가로(열), 세로(행)
N, M = map(int, input().split()) # 로봇 개수, 명령 개수

dir_dict = {
    'N': 0,
    'E': 1,
    'S': 2,
    'W': 3
}

robots = []
for _ in range(N):
    x, y, d = input().split()
    r = B - int(y)
    c = int(x) - 1
    d = dir_dict[d]
    robots.append([r, c, d])

#     북  동  남  서
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

for _ in range(M):
    robot, command, repeat = input().split()
    robot = int(robot)
    repeat = int(repeat)
    r, c, d = robots[robot-1]

    for _ in range(repeat):
        if command == 'L': # 왼쪽으로 90도 회전
            d = (d-1) % 4
        elif command == 'R': # 오른쪽으로 90도 회전
            d = (d+1) % 4
        elif command == 'F': # 앞으로 한 칸 이동
            r += dr[d]
            c += dc[d]

            if not (0 <= r < B and 0 <= c < A):
                print(f'Robot {robot} crashes into the wall')
                exit(0)

            else:
                for i in range(N):
                    if i != robot-1:
                        if r == robots[i][0] and c == robots[i][1]:
                            print(f'Robot {robot} crashes into robot {i+1}')
                            exit(0)

    robots[robot-1] = [r, c, d]

print('OK')
