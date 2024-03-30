import sys

input = sys.stdin.readline

n, m = map(int, input().split())

matrixA = []
for _ in range(n):
    matrixA.append(list(map(int, input().rstrip())))

matrixB = []
for _ in range(n):
    matrixB.append(list(map(int, input().rstrip())))

def reverse_matrix(y, x):
    for i in range(y, y + 3):
        for j in range(x, x + 3):
            matrixA[i][j] = 1 - matrixA[i][j]

count = 0
for row in range(n - 2):
    for col in range(m - 2):
        if matrixA[row][col] != matrixB[row][col]:
            reverse_matrix(row, col)
            count += 1

if matrixA != matrixB:
    count = -1

print(count)
