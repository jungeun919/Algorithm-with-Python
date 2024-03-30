# import sys

# input = sys.stdin.readline

# n, m = map(int, input().split())

# graph = []

# for _ in range(n):
#     graph.append(list(map(int, input().split())))

# def accumulate_sum(x1, y1, x2, y2):
#     sum = 0
#     for row in range(x1 - 1, x2):
#         for col in range(y1 - 1, y2):
#             sum += graph[row][col]
#     return sum

# for _ in range(m):
#     x1, y1, x2, y2 = map(int, input().split())
#     print(accumulate_sum(x1, y1, x2, y2))

# 1차원 누적합
# S[i] = a[0] + a[1] + ... + a[i]
# a[i] + ... + a[j] = S[j] - S[i - 1]
# S[i] = S[i - 1] + a[i]

# 2차원 누적합
# D[i][j] = D[i - 1][j] + D[i][j - 1] - D[i - 1][j - 1] + A[i][j]

import sys

input = sys.stdin.readline

n, m = map(int, input().split())

graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))

dp = [[0] * (n + 1) for _ in range(n + 1)]

for row in range(1, n + 1):
    for col in range(1, n + 1):
        dp[row][col] = dp[row - 1][col] + dp[row][col - 1] - dp[row - 1][col - 1] + graph[row - 1][col - 1]

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    res = dp[x2][y2] - dp[x1 - 1][y2] - dp[x2][y1 - 1] + dp[x1 - 1][y1 - 1]
    print(res)
