import sys

input = sys.stdin.readline

n = int(input())

res = 0
row = [0] * n

def is_promising(x):
    for i in range(x):
        # 같은 열, 대각선 체크
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):
            return False
    return True

def nqueens(x):
    global res
    
    if x == n:
        res += 1
        return

    for i in range(n):
        row[x] = i # (x, i)에 퀸 놓기
        if is_promising(x) == True:
            nqueens(x + 1) # 다음 행에 퀸 놓기

nqueens(0)

print(res)
