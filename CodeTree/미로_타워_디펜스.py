n, m = map(int, input().split())

board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

# 달팽이 모양 방향으로 몬스터 번호 담기
def manage_monster_position():
    #          하  우  상  좌
    move_dr = [1, 0, -1, 0]
    move_dc = [0, 1, 0, -1]

    move_count, move_dir = 1, 0

    r, c = n//2, n//2 - 1 # 플레이어 제외
    monster.append([r, c])

    while True:
        for _ in range(move_count):
            r += move_dr[move_dir]
            c += move_dc[move_dir]
            if r == 0 and c == -1:
                return
            monster.append([r, c])
        
        if move_dir == 0 or move_dir == 2:
            move_count += 1
        
        move_dir = (move_dir + 1) % 4

#     우  하  좌  상
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

# d방향으로 p칸만큼 몬스터 제거
def attack_monster(d, p):
    monster_r, monster_c = n//2, n//2
    score = 0

    for _ in range(p):
        monster_r += dr[d]
        monster_c += dc[d]

        if 0 <= monster_r < n and 0 <= monster_c < n:
            score += board[monster_r][monster_c]
            board[monster_r][monster_c] = 0
    
    return score

# 비어있는 공간만큼 앞으로 이동했을 때의 몬스터 번호 담기
def pull_monster():
    monster_num = []
    for r, c in monster:
        if board[r][c] != 0:
            monster_num.append(board[r][c])
    return monster_num

# 같은 종류가 4번 반복하면 삭제 후 몬스터 번호 담기
def check_four_sequence(monster_num):
    global score

    while True:
        curr_num = monster_num[0]
        sequence = 1
        find_four_sequence = False
        update_monster_num = []

        for i in range(1, len(monster_num)):
            if curr_num != monster_num[i]:
                if sequence < 4:
                    update_monster_num += ([curr_num] * sequence)
                else:
                    find_four_sequence = True
                    score += (curr_num * sequence)
                curr_num = monster_num[i]
                sequence = 1
            else:
                sequence += 1
        
        if sequence < 4:
            update_monster_num += [curr_num] * sequence
        else:
            find_four_sequence = True
            score += (curr_num * sequence)
        
        if find_four_sequence == False:
            break
        
        monster_num = update_monster_num
    
    return update_monster_num

# (개수, 몬스터 번호) 쌍으로 몬스터 번호 담기
def get_pair_monster_num(monster_num):
    curr_num = monster_num[0]
    count = 1

    pair_monster_num = []
    for i in range(1, len(monster_num)):
        if curr_num != monster_num[i]:
            pair_monster_num.append(count)
            pair_monster_num.append(curr_num)
            curr_num = monster_num[i]
            count = 1
        else:
            count += 1
    pair_monster_num.append(count)
    pair_monster_num.append(curr_num)
    return pair_monster_num

# 다시 세팅하기
def set_board(monster_num):
    for i, (r, c) in enumerate(monster):
        if i >= len(monster_num):
            board[r][c] = 0
        else:
            board[r][c] = monster_num[i]

monster = []
manage_monster_position()

score = 0

for _ in range(m):
    d, p = map(int, input().split())

    score += attack_monster(d, p)
    monster_num = pull_monster()
    update_monster_num = check_four_sequence(monster_num)
    next_monster_num = get_pair_monster_num(update_monster_num)
    set_board(next_monster_num)

print(score)
