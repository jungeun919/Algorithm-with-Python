N, M, K = map(int, input().split())

maze = []
maze.append([-1] * (N+1))
for _ in range(1, N+1):
    maze.append([-1] + list(map(int, input().split())))

people = []
for _ in range(M):
    people.append(list(map(int, input().split())))

exit = list(map(int, input().split()))

#     상  하  좌  우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

move_dist = 0

def move_people():
    global people, move_dist

    for i in range(len(people)):
        dist = abs(people[i][0] - exit[0]) + abs(people[i][1] - exit[1])
        for j in range(4):
            nr = people[i][0] + dr[j]
            nc = people[i][1] + dc[j]
            if 1 <= nr <= N and 1 <= nc <= N:
                if (maze[nr][nc] == 0) or (nr == exit[0] and nc == exit[1]):
                    if dist > abs(nr - exit[0]) + abs(nc - exit[1]):
                        move_dist += 1
                        people[i] = [nr, nc]
                        break

def find_min_square():
    for size in range(1, N+1):
        for r1 in range(1, N-size+2):
            for c1 in range(1, N-size+2):
                r2 = r1+size-1
                c2 = c1+size-1

                # 출구가 포함되지 않을 경우
                if not(r1 <= exit[0] <= r2 and c1 <= exit[1] <= c2):
                    continue
                
                # 한 명 이상의 참가자가 포함될 경우
                for i in range(len(people)):
                    if r1 <= people[i][0] <= r2 and c1 <= people[i][1] <= c2:
                        if not(people[i][0] == exit[0] and people[i][1] == exit[1]):
                            return [r1, c1, size]
    return [0, 0, 0]

def rotate_square(r1, c1, size):
    global maze, people, exit

    rotate_maze = [row[:] for row in maze]
    # 시계방향으로 90도 회전
    for i in range(size):
        for j in range(size):
            rotate_maze[r1 + j][c1 + size - 1 - i] = maze[r1 + i][c1 + j]
            if maze[r1 + i][c1 + j] > 0:
                rotate_maze[r1 + j][c1 + size - 1 - i] -= 1
    maze = rotate_maze
    
    # people 위치 업데이트
    for i in range(len(people)):
        pr, pc = people[i]
        if r1 <= pr <= r1+ size - 1 and c1 <= pc <= c1 + size - 1:
            new_pr = r1 + (pc - c1)
            new_pc = c1 + size - 1 - (pr - r1)
            people[i] = [new_pr, new_pc]
    
    # exit 위치 업데이트
    if r1 <= exit[0] <= r1 + size - 1 and c1 <= exit[1] <= c1 + size - 1:
        new_er = r1 + (exit[1] - c1)
        new_ec = c1 + size - 1 - (exit[0] - r1)
        exit = [new_er, new_ec]
    

for i in range(K):
    move_people()

    all_exit = True
    for i in range(len(people)):
        if people[i] != exit:
            all_exit = False
            break
    
    if all_exit == True:
        break
    
    r1, c1, size = find_min_square()
    rotate_square(r1, c1, size)

print(move_dist)
print(exit[0], exit[1])
