import sys

input = sys.stdin.readline

# n = 2, m = 4
#    0  1  2  3  4
# 0 [1, 1, 1, 1, 1]
# 1 [1, 1, 2, 3, 4]
# 2 [1, 1, 1, 3, 6]

T = int(input())

for _ in range(T):
    n, m = map(int, input().split()) # n <= m
    dp = [[1 for _ in range(m + 1)] for _ in range(n + 1)]

    for i in range(1, m + 1):
        dp[1][i] = i

    for row in range(2, n + 1):
        for col in range(row + 1, m + 1):
            dp[row][col] = dp[row][col - 1] + dp[row - 1][col - 1]

    print(dp[n][m])
