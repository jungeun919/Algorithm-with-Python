n, m, q = map(int, input().split())

board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

def rotate(row, d, k):
    # 상 좌 하 우 (시계 방향으로 배열에 저장)
    temp = [0] * m
    
    #   1                       4
    # 4   2  -> (d=0, k=1) -> 3   1
    #   3                       2
    # [1, 2, 3, 4] -> [4, 1, 2, 3]

    #   1                       2
    # 4   2  -> (d=1, k=1) -> 1   3
    #   3                       4
    # [1, 2, 3, 4] -> [2, 3, 4, 1]

    if d == 0: # 시계 방향
        for col in range(m):
            temp[(col + k) % m] = board[row][col]
    elif d == 1: # 반시계 방향
        for col in range(m):
            temp[(col - k + m) % m] = board[row][col]
    
    for col in range(m):
        board[row][col] = temp[col]

#     상  하  좌  우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def remove():
    is_removed = False
    same = [[False] * m for _ in range(n)]

    for r in range(n):
        for c in range(m):
            if board[r][c] == 0:
                continue
            
            for d in range(4):
                nr = r + dr[d]
                nc = (c + dc[d]) % m
                if 0 <= nr < n and 0 <= nc < m:
                    if board[r][c] == board[nr][nc]:
                        same[r][c] = True
                        same[nr][nc] = True
    
    for r in range(n):
        for c in range(m):
            if same[r][c] == True:
                is_removed = True
                board[r][c] = 0
    
    return is_removed

def normalize():
    total, count = 0, 0
    for r in range(n):
        for c in range(m):
            if board[r][c] != 0:
                total += board[r][c]
                count += 1
    
    if count == 0:
        return
    
    avg = total // count

    for r in range(n):
        for c in range(m):
            if board[r][c] != 0:
                if board[r][c] > avg:
                    board[r][c] -= 1
                elif board[r][c] < avg:
                    board[r][c] += 1

for _ in range(q):
    x, d, k = map(int, input().split())

    # 원판의 번호가 x의 배수일 경우 회전
    for i in range(n):
        if (i+1) % x == 0:
            rotate(i, d, k)
    
    if remove() == False:
        normalize()

total = 0
for r in range(n):
    for c in range(m):
        total += board[r][c]
print(total)
