import sys

input = sys.stdin.readline

n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]

minus = 0
zero = 0
plus = 0

def divide(row, col, n):
    global minus, zero, plus
    
    find = paper[row][col]
    
    for i in range(row, row + n):
        for j in range(col, col + n):
            if find != paper[i][j]:
                for a in range(3):
                    for b in range(3):
                        divide(row + a * n//3, col + b * n//3, n//3)
                return
    
    if find == -1:
        minus += 1
    elif find == 0:
        zero += 1
    elif find == 1:
        plus += 1
    
divide(0, 0, n)

print(minus, zero, plus, sep="\n")
