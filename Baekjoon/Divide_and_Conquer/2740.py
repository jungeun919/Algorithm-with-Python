# A : N * M
# B : M * K
# res : N * K

# (3, 2) * (2, 3)
# (1,1)*(1,1) + (1,2)*(2,1) | (1,1)*(1,2) + (1,2)*(2,2) | (1,1)*(1,3) + (1,2)*(2,3)
# (2,1)*(1,1) + (2,2)*(2,1) | (2,1)*(1,2) + (2,2)*(2,2) | (2,1)*(1,3) + (2,2)*(2,3)
# (3,1)*(1,1) + (3,2)*(2,1) | (3,1)*(1,2) + (3,2)*(2,2) | (3,1)*(1,3) + (3,2)*(2,3)

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
matrixA = []
for _ in range(n):
    matrixA.append(list(map(int, input().split())))
    
m, k = map(int, input().split())
matrixB = []
for _ in range(m):
    matrixB.append(list(map(int, input().split())))

matrixC = [[0] * k for _ in range(n)]
for nn in range(n):
    for kk in range(k):
        for mm in range(m):
            matrixC[nn][kk] += matrixA[nn][mm] * matrixB[mm][kk]
            
for row in matrixC:
    print(" ".join(list(map(str, row))))
