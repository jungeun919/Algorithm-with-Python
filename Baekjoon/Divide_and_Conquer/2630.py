import sys

input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

white = 0
blue = 0

# divide
def sol(row, col, n):
    # print("row, col, n:", row, col, n)
    global white, blue
    
    color = board[row][col]
    
    for i in range(row, row + n):
        for j in range(col, col + n):
            if color != board[i][j]:
                # print("i, j, n:", i, j, n)
                sol(row, col, n//2)
                sol(row, col + n//2, n//2)
                sol(row + n//2, col, n//2)
                sol(row + n//2, col + n//2, n//2)
                return
    
    if color == 0:
        white += 1
    else:
        blue += 1
    # print("white, blue, n:", white, blue, n)
    # print()

sol(0, 0, n)

print(white)
print(blue)
