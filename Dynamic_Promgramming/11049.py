import sys

input = sys.stdin.readline

n = int(input())
matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split()))) # [row, col]

dp = [[0] * n for _ in range(n)]

for d in range(1, n): # 대각선
    for start in range(n - d):
        end = start + d
        
        dp[start][end] = 2 ** 31
        for k in range(start, end):
            dp[start][end] = min(dp[start][end], \
                        dp[start][k] + dp[k + 1][end] + matrix[start][0] * matrix[k][1] * matrix[end][1])

print(dp[0][n - 1])
